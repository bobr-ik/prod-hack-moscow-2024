from sqlalchemy import select, and_, func, insert, or_, not_
from data.database import sync_engine, session_factory, Base
from data.models import DebtsHistoryORM
from bot.handlers import send_notification


class SyncORM:
    @staticmethod
    def create_table():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
    
        
    @staticmethod
    def insert_data():
        with session_factory() as session:
            create = [
    {
        "f_tg_tag_debtor": "@ivan",
        "f_tg_tag_lender": "@petr",
        "f_debt_amount": 150
    },
    {
        "f_tg_tag_debtor": "@ivan",
        "f_tg_tag_lender": "@petr",
        "f_debt_amount": 200
    },
    {
        "f_tg_tag_debtor": "@ivan",
        "f_tg_tag_lender": "@oleg",
        "f_debt_amount": 50
    },
    {
        "f_tg_tag_debtor": "@sveta",
        "f_tg_tag_lender": "@petr",
        "f_debt_amount": 150
    },
    {
        "f_tg_tag_debtor": "@sveta",
        "f_tg_tag_lender": "@oleg",
        "f_debt_amount": 75
    },
    {
        "f_tg_tag_debtor": "@petr",
        "f_tg_tag_lender": "@ivan",
        "f_debt_amount": 300
    },
    {
        "f_tg_tag_debtor": "@oleg",
        "f_tg_tag_lender": "@ivan",
        "f_debt_amount": 25
    },
    {
        "f_tg_tag_debtor": "@oleg",
        "f_tg_tag_lender": "@sveta",
        "f_debt_amount": 100
    }
]
            insert_data = insert(DebtsHistoryORM).values(create)
            session.execute(insert_data)
            session.commit()
    

    @staticmethod
    def get_user_history(lender_tg, debtor_tg):
        with session_factory() as session:
            query = select(DebtsHistoryORM).where(and_(DebtsHistoryORM.f_tg_tag_debtor == debtor_tg, DebtsHistoryORM.f_tg_tag_lender == lender_tg))
            res = session.execute(query)
            history = res.scalars().all() 
            if history:
                return list(map(lambda x: {'amount': x.f_debt_amount, 'event_name': x.f_event_name, 'event_date': x.f_event_date}, history))
            return []

    @staticmethod
    def get_user_debtors(lender_tg):
        # -> tg должников и сумма
        with session_factory() as session:
            # кто должен lender_tg и сколько
            subq = select(DebtsHistoryORM.f_tg_tag_debtor.label('tg_tag_debtor'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(DebtsHistoryORM.f_tg_tag_lender == lender_tg).group_by(DebtsHistoryORM.f_tg_tag_debtor).subquery()
            subq_res = {elem[0]: elem[1] for elem in session.execute(select(subq)).all()}
            # кому должен lender_tg и сколько
            subq1 = select(DebtsHistoryORM.f_tg_tag_lender.label('tg_tag_lender'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(DebtsHistoryORM.f_tg_tag_debtor == lender_tg).group_by(DebtsHistoryORM.f_tg_tag_lender).subquery()
            # вычитание тех, кого можно вычесть
            subq2 = select(subq.c.tg_tag_debtor, (subq.c.debt_amount-subq1.c.debt_amount).label('debt_amount')).where(or_(and_(subq.c.tg_tag_debtor == subq1.c.tg_tag_lender, subq.c.debt_amount-subq1.c.debt_amount > 0), not_(subq.c.tg_tag_debtor.in_(subq_res.keys())))).subquery()
            subq2_res = {elem[0]: elem[1] for elem in session.execute(select(subq2)).all()}
            #красотаааааа
            ans = []
            for elem in subq_res.keys():
                if elem in subq2_res:
                    ans.append({'debtor_tg': elem, 'amount': subq2_res[elem]})
                else:
                    ans.append({'debtor_tg': elem, 'amount': subq_res[elem]})
            return ans
        

    @staticmethod
    def get_user_lenders(debtor_tg):
        # -> tg кому должен и сумма
        with session_factory() as session:
            # кто должен debter_tg и сколько
            subq = select(DebtsHistoryORM.f_tg_tag_debtor.label('tg_tag_debtor'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(DebtsHistoryORM.f_tg_tag_lender == debtor_tg).group_by(DebtsHistoryORM.f_tg_tag_debtor).subquery()
            # кому должен debter_tg и сколько
            subq1 = select(DebtsHistoryORM.f_tg_tag_lender.label('tg_tag_lender'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(DebtsHistoryORM.f_tg_tag_debtor == debtor_tg).group_by(DebtsHistoryORM.f_tg_tag_lender).subquery()
            subq_res = {elem[0]: elem[1] for elem in session.execute(select(subq1)).all()}
            # вычитание тех, кого можно вычесть
            subq2 = select(subq.c.tg_tag_debtor, (subq1.c.debt_amount - subq.c.debt_amount).label('debt_amount')).where(or_(and_(subq.c.tg_tag_debtor == subq1.c.tg_tag_lender, subq1.c.debt_amount - subq.c.debt_amount > 0))).subquery()
            subq2_res = {elem[0]: elem[1] for elem in session.execute(select(subq2)).all()}
            #красотаааааа
            ans = []
            for elem in subq_res.keys():
                if elem in subq2_res:
                    ans.append({'debtor_tg': elem, 'amount': subq2_res[elem]})
                else:
                    ans.append({'debtor_tg': elem, 'amount': subq_res[elem]})
            return ans
    
    
    @staticmethod
    def insert_debt(lender_tg, debtors_tg_debpt_dict, event_name, event_date):
        with session_factory() as session:
            for debtor, amount in debtors_tg_debpt_dict:
                create = DebtsHistoryORM(f_tg_tag_lender=lender_tg, f_tg_tag_debtor=debtor, f_debt_amount=amount, f_event_name=event_name, f_event_date=event_date)
                session.add(create)
                send_notification(debtor=debtor, lender_tg=lender_tg, event_name=event_name, event_date=event_date)

            session.commit()
