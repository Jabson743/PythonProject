import unittest
from Python_Practices import loancontract

class TestContractLoan(unittest.TestCase):
    def setUp(self):
        self.loan = loancontract.LoanContract()

    def test_that_contract_loan_app_exist(self):
        exist = loancontract.LoanContract()
        self.assertTrue( self.loan, exist)

    def test_that_contract_loan_app_can_get_monthly_rate(self):
        monthly_rate = self.loan.get_monthly_rate(0.0125)
        self.assertEqual(monthly_rate, 0.0125)

    def test_that_contract_loan_app_can_get_borrower_details(self):
        borrower = loancontract.LoanContract()
        self.assertTrue(borrower)

    def test_that_contract_loan_app_can_get_monthly_duration(self):
        duration = self.loan.get_monthly_duration()
        self.assertEqual(duration, 24)

    def test_that_contract_loan_app_can_get_monthly_payment(self):
        monthly_payment = self.loan.get_monthly_payment()
        self.assertEqual(monthly_payment, 9697.33)

    def test_that_contract_loan_app_can_get_total_payment(self):
        total_payment = self.loan.get_total_payment(9697.33, 24)
        self.assertEqual(total_payment, 232736.0)