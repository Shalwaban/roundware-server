from django.test import TestCase
from django.conf import settings

from model_mommy import mommy
from model_mommy.generators import gen_file_field

from roundware.settings import DEFAULT_SESSION_ID
from roundware.rw.models import (UIMode, Language, LocalizedString, 
                                 Tag, TagCategory, Session)


def rw_validated_file_field_gen():
    return gen_file_field()


class FakeRequest():
    pass


class RoundwaredTestCase(TestCase):
    """ provide common testcase data for Roundwared test cases 
    """

    def setUp(self):
        self.maxDiff = None

        generator_dict = {
            'roundware.rw.fields.RWValidatedFileField': 
            rw_validated_file_field_gen
        }
        # can't set this directly in settings: db ENGINE not yet available
        setattr(settings, 'MOMMY_CUSTOM_FIELDS_GEN', generator_dict)

        self.default_session = mommy.make(Session, id=DEFAULT_SESSION_ID)
        self.ui_mode_listen = mommy.make(UIMode, name="listen")
        self.ui_mode_speak = mommy.make(UIMode, name="speak")
        self.english = mommy.make(Language, language_code='en')
        self.spanish = mommy.make(Language, language_code='es')
        self.english_msg = mommy.make(LocalizedString, localized_string="One",
                                      language=self.english)
        self.spanish_msg = mommy.make(LocalizedString, localized_string="Uno",
                                      language=self.spanish)
        self.tagcat1 = mommy.make(TagCategory)
        self.tag1 = mommy.make(Tag, data="{'json':'value'}",
                               loc_msg=[self.english_msg, self.spanish_msg],
                               tag_category=self.tagcat1,
                               value='tag1')
