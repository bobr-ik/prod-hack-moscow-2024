from typing import Optional
from sqlalchemy import Table, Column, Integer, String, MetaData, Numeric, ForeignKey, text, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data.database import Base
from datetime import datetime, timezone


metadata_obj = MetaData()


class DebtsHistoryORM(Base):
    __tablename__ = "t_debts"
    f_id: Mapped[int] = mapped_column(primary_key=True)
    f_debt_amount: Mapped[int]
    f_tg_tag_lender: Mapped[str] = mapped_column(String(50))
    f_tg_tag_debtor: Mapped[str] = mapped_column(String(50))
    f_event_name: Mapped[str] = mapped_column(String(50))
    f_event_date: Mapped[datetime] = mapped_column(datetime.now(timezone.utc))


class TripsORM(Base):
    __tablename__ = "t_trips"
    f_id: Mapped[int] = mapped_column(primary_key=True)
    f_trip_name: Mapped[str] = mapped_column(String(50))
    f_start_date: Mapped[datetime] = mapped_column(datetime.now(timezone.utc))
    f_end_date: Mapped[Optional[datetime]]
    f_is_ended: Mapped[bool] = mapped_column(default=False)


class TripDebtsORM(Base):
    __tablename__ = "t_trip_debts"
    f_id: Mapped[int] = mapped_column(primary_key=True)
    f_trip_id: Mapped[int] = mapped_column(ForeignKey("t_trips.f_id"))
    f_debt_amount: Mapped[int]
    f_tg_tag_lender: Mapped[str] = mapped_column(String(50))
    f_tg_tag_debtor: Mapped[str] = mapped_column(String(50))
    f_event_name: Mapped[str] = mapped_column(String(50))
    f_event_date: Mapped[datetime] = mapped_column(datetime.now(timezone.utc))

