from typing import Optional
from sqlalchemy import Table, Column, Integer, String, MetaData, Numeric, ForeignKey, text, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.database import Base


metadata_obj = MetaData()


class DebtsHistoryORM(Base):
    __tablename__ = "t_debts"
    f_id: Mapped[int] = mapped_column(primary_key=True)
    f_debt_amount: Mapped[int]
    f_tg_tag_lender: Mapped[str] = mapped_column(String(50))
    f_tg_tag_debtor: Mapped[str] = mapped_column(String(50))
    f_event_name: Mapped[str] = mapped_column(String(50))
    f_event_date: Mapped[str] = mapped_column(String(50))
