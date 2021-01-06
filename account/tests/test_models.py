from django.test import TestCase,Client
from account.models import User, superMassage, Customer, Business, Categories

class TestModels(TestCase):

    def setUp(self):
        #   Create objects
        self.superMassageObj = superMassage.objects.create(
            super_Massage = 'message'
        )
        self.UserObj = User.objects.create(
            is_customer = True,
            is_business = False,
            first_name = 'Jim',
            last_name = 'Botten'
        )
        self.CustomerObj = Customer.objects.create(
            user = self.UserObj,
            address = 'Bazel',
            phone = '0509998852',
            age = '16'
        )
        self.BusinessObj = Business.objects.create(
            user = self.UserObj,
            business_name = 'Zoglovek',
            business_address = 'Hash',
            business_phone = '0528847793',
            business_info = 'info_info',
            business_category = 'Naknikim',
            business_massage = 'Special message',
            business_deals = 'Special deal',
        )
        self.CategoriesObj = Categories.objects.create(
            category_name = 'Computers'
        )

    #   Tests methods
    def test_superMassage(self):
        self.assertEqual(self.superMassageObj.super_Massage, 'message')
        self.assertEqual(self.superMassageObj.__str__(), 'superMassage: {}'.format(self.superMassageObj.super_Massage))
    
    def test_User(self):
        self.assertTrue(self.UserObj.is_customer)
        self.assertFalse(self.UserObj.is_business)
        self.assertEqual(self.UserObj.first_name, 'Jim')
        self.assertEqual(self.UserObj.last_name, 'Botten')
        self.assertNotEqual(self.UserObj.first_name, 'Jil')

    def test_Customer(self):
        self.assertTrue(self.CustomerObj.user.is_customer)
        self.assertFalse(self.CustomerObj.user.is_business)
        self.assertEqual(self.CustomerObj.address, 'Bazel')
        self.assertEqual(self.CustomerObj.phone, '0509998852')
        self.assertNotEqual(self.CustomerObj.phone, '0509998851')
        self.assertEqual(self.CustomerObj.age, '16')
        self.assertEqual(self.CustomerObj.__str__(), 'user: {}'.format(self.CustomerObj.user))

    def test_Business(self):
        self.assertTrue(self.BusinessObj.user.is_customer)
        self.assertFalse(self.BusinessObj.user.is_business)
        self.assertEqual(self.BusinessObj.business_name, 'Zoglovek')
        self.assertEqual(self.BusinessObj.business_address, 'Hash')
        self.assertEqual(self.BusinessObj.business_phone, '0528847793')
        self.assertEqual(self.BusinessObj.business_info, 'info_info')
        self.assertEqual(self.BusinessObj.business_category, 'Naknikim')
        self.assertEqual(self.BusinessObj.business_massage, 'Special message')
        self.assertNotEqual(self.BusinessObj.business_massage, 'Specialmessage')
        self.assertEqual(self.BusinessObj.business_deals, 'Special deal')
        self.assertEqual(self.BusinessObj.get_Business_Name(), 'Zoglovek')
        self.assertEqual(self.BusinessObj.__str__(), 'business_name: {}'.format(self.BusinessObj.business_name))

    def test_Categories(self):
        self.assertEqual(self.CategoriesObj.category_name, 'Computers')
        self.assertNotEqual(self.CategoriesObj.category_name, 'Computerz')
        self.assertEqual(self.CategoriesObj.__str__(), self.CategoriesObj.category_name)