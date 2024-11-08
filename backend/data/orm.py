from sqlalchemy import select, and_, func, insert
from data.database import sync_engine, session_factory, Base
from data.models import DebtsHistoryORM


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
        "f_debt_amount": 100
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
            query = select(DebtsHistoryORM.f_tg_tag_debtor, func.sum(DebtsHistoryORM.f_debt_amount).label('debt_amount')).where(DebtsHistoryORM.f_tg_tag_lender == lender_tg).group_by(DebtsHistoryORM.f_tg_tag_debtor)
            res = session.execute(query).all()
            return list(map(lambda x: {'debtor_tg': x.f_tg_tag_debtor,'amount': x.debt_amount}, res))
            


    @staticmethod
    def insert_debt(lender_tg, debtor_tg, amount, event_name, event_date):
        with session_factory() as session:
            create = DebtsHistoryORM(f_tg_tag_lender=lender_tg, f_tg_tag_debtor=debtor_tg, f_debt_amount=amount, f_event_name=event_name, f_event_date=event_date)
            session.add(create)
            session.commit()
            return 0
    
    
    
