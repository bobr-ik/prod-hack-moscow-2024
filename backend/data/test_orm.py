import unittest

from data.orm import SyncORM

class TestORM(unittest.TestCase):

    def test_get_user_history(self, lender_tg, debtor_tg):
        #Просто суммы
        self.assertEqual(SyncORM.get_user_history('@petr', '@ivan')[0]['amount'], 150)
        self.assertEqual(SyncORM.get_user_history('@petr', '@ivan')[1]['amount'], 200)
    
    def test_get_user_debtors(self):
        #http://127.0.0.1:5000/get_user_debtors?lender_tg=@petr

        #Должники Петра
        self.assertEqual(SyncORM.get_user_debtors('@petr')[0]['debtor_tg'], '@ivan')
        self.assertEqual(SyncORM.get_user_debtors('@petr')[0]['amount'], '50')

        self.assertEqual(SyncORM.get_user_debtors('@petr')[1]['debtor_tg'], '@sveta')
        self.assertEqual(SyncORM.get_user_debtors('@petr')[1]['amount'], '150')

        #а ивану никто ничего не должен
        #http://127.0.0.1:5000/get_user_debtors?lender_tg=@ivan
        self.assertEqual(SyncORM.get_user_debtors('@ivan'), [])

        



    def test_get_user_lenders(self, debtor_tg):
        #petr никому ничего не должен
        #http://127.0.0.1:5000/get_user_lenders?debtor_tg=@petr
        self.assertEqual(SyncORM.get_user_lenders('@petr'), [])

        #http://127.0.0.1:5000/get_user_lenders?debtor_tg=@ivan
        #Кому должен ivan
        self.assertEqual(SyncORM.get_user_lenders('@ivan')[0]['lenders_tg'], '@oleg')
        self.assertEqual(SyncORM.get_user_lenders('@ivan')[0]['amount'], '25')

        self.assertEqual(SyncORM.get_user_lenders('@ivan')[1]['lenders_tg'], '@petr')
        self.assertEqual(SyncORM.get_user_lenders('@ivan')[1]['amount'], '50')

