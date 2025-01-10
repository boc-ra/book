import datetime
from django.test import TestCase
from .models import Bookdiary


class DiaryModelTests(TestCase):

    def test_bookdiary_has_date(self):
        """
        作成した日記データに日付が付与されているか確認        
        """
        Bookdiary.objects.create(title='test_title', text='test_text')
        actual_diary = Bookdiary.objects.get(title='test_title')
        self.assertIsInstance(actual_diary.date, datetime.date)

    def test_save_and_retrieve(self):
        """
        日記データの保存と取得を確認
        """
        Bookdiary.objects.create(title='test_title', text='test_text')
        actual_diary = Bookdiary.objects.get(title='test_title')
        self.assertEqual(actual_diary.title, 'test_title')