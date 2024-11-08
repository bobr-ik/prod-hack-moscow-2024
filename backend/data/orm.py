from sqlalchemy import select, and_, func, insert
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
    def get_user_debts(lender_tg):
        with session_factory() as session:
            subq = select(DebtsHistoryORM.f_tg_tag_debtor.label('tg_tag_debtor'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(DebtsHistoryORM.f_tg_tag_lender == lender_tg).group_by(DebtsHistoryORM.f_tg_tag_debtor).subquery()
            subq1 = select(DebtsHistoryORM.f_tg_tag_lender.label('tg_tag_lender'), func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(DebtsHistoryORM.f_tg_tag_debtor == lender_tg).group_by(DebtsHistoryORM.f_tg_tag_lender).subquery()

            query = select(subq.c.tg_tag_debtor, (subq.c.debt_amount-subq1.c.debt_amount).label('debt_amount'))
            # .where(and_(subq.c.tg_tag_debtor == lender_tg, subq1.c.tg_tag_lender == lender_tg)
            # query = select(subq1.c.tg_tag_lender, subq1.c.debt_amount)
            res = session.execute(query).all()
            print(res)
            return list(map(lambda x: {'debtor_tg': x.tg_tag_debtor,'amount': x.debt_amount}, res))
            

    
    @staticmethod
    def insert_debt(lender_tg, debtors_tg_debpt_dict, event_name, event_date):
        with session_factory() as session:
            for debtor, amount in debtors_tg_debpt_dict:
                create = DebtsHistoryORM(f_tg_tag_lender=lender_tg, f_tg_tag_debtor=debtor, f_debt_amount=amount, f_event_name=event_name, f_event_date=event_date)
                session.add(create)
                send_notification(debtor=debtor, lender_tg=lender_tg, event_name=event_name, event_date=event_date)

            session.commit()
