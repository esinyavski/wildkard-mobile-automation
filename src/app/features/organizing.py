import time
import pytest

from src.app.features.common import Common
from src.app.constants import Role


class Organizing(Common):

    def __init__(self, **kwargs):
        super().__init__(page=__class__.__name__, **kwargs)

    def validate(self):
        self.find_element_by_accessibility_id('To Do').is_displayed()

    def go_to_dashboard(self):
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="ORGANIZER_DASHBOARD, tab, 1 of 5"]').click()

    def go_to_search(self):
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="ORGANIZER_SEARCH, tab, 2 of 5"]').click()
        self.find_element_by_accessibility_id('Search for athletes and teams').is_displayed()

    def go_to_create_menu(self):
        time.sleep(0.5)
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="ORGANIZER_CREATE, tab, 3 of 5"]').click()

    def go_to_games(self):
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="ORGANIZER_GAMES, tab, 4 of 5"]').click()
        self.find_element_by_accessibility_id('Games').is_displayed()

    def go_to_amplify(self):
        self.find_element_by_xpath('//XCUIElementTypeButton[@name="ORGANIZER_AMPLIFY, tab, 4 of 5"]').click()

    def click__profile(self):
        self.find_element_by_xpath('//XCUIElementTypeOther[@name=""]').click()

    def click__settings(self):
        self.find_element_by_xpath('//XCUIElementTypeStaticText[@name=""]').click()

    def add_official_to_league(self, user):
        # type the user
        self.send_keys(el=self.find_element_by_accessibility_id('Phone number, name, or add from contacts'),
                       data=user.number)
        self.find_element_by_xpath(f'//XCUIElementTypeOther[@name="{user.full_number}"]').click()
        # select the role
        self.find_element_by_accessibility_id('ios_touchable_wrapper').click()
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypePicker[@name="ios_picker"]'),
                       data=Role.Official.value)
        # send invitation
        self.find_element_by_accessibility_id('Send invitation').click()
        self.find_element_by_accessibility_id('Officials invited!').is_displayed()

    def click__create_team(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="leaguesSheetLeagueButton"])[2]').click()

    def upload_logo_from_gallery(self):
        self.find_element_by_accessibility_id('難 Upload logo').click()
        self.find_element_by_accessibility_id('Wildkard').click()
        self.find_element_by_xpath(
            '//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell').click()

    def determine_logo_by_wildkard(self):
        self.find_element_by_xpath('//*[@name="Let WildKard determine logo"]/XCUIElementTypeOther').click()

    def enter_team_name(self, name=None):
        self.send_keys(el=self.find_element_by_xpath('//*[@name="Enter team name"]'),
                       data=name if name else self.dummy.gen_string())

    def click__create(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="Create"])[2]').click()

    def click__ok(self):
        self.find_element_by_accessibility_id('OK').click()

    def create_team(self, name, user=None, upload_logo=False):
        self.click__create_team()
        self.enter_team_name(name)
        self.find_element_by_xpath('//*[@name="or"]').click()
        time.sleep(1)
        if "Team name taken. Please type in a new team name" in self.driver.page_source:
            pytest.skip("Team name taken. Please clean app's DB before test run")
        if upload_logo:
            self.upload_logo_from_gallery()
        else:
            self.determine_logo_by_wildkard()
        if user:
            self.find_element_by_xpath('(//XCUIElementTypeOther[@name=" Add athletes (optional) "])[2]').click()
            self.send_keys(el=self.find_element_by_accessibility_id('Phone number, name, or add from contacts'),
                           data=user.number)
            self.find_element_by_xpath(f'//XCUIElementTypeOther[@name="{user.full_number}"]').click()
        self.click__create()
        self.find_element_by_accessibility_id('Team created').is_displayed()
        self.click__ok()

    def click__invite_athletes(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="leaguesSheetLeagueButton"])[1]').click()

    def click__select_users(self):
        self.find_element_by_accessibility_id('').click()

    def search_for_users(self, value):
        self.send_keys(el=self.find_element_by_xpath('//*[@name=" Search "]'),
                       data=value)

    def edit_team(self, name, user):
        # search
        self.send_keys(el=self.find_element_by_xpath('//*[@name="Search"]'),
                       data=self.dummy.FILTER_KEY)
        self.find_element_by_xpath(f'//XCUIElementTypeOther[@name="{name}"]').click()

        # rename
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypeTextField'),
                       data='upd')

        # add athlete
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name=" Add athletes "])[3]').click()
        self.send_keys(el=self.find_element_by_accessibility_id('Phone number, name, or add from contacts'),
                       data=user.number)
        self.find_element_by_xpath(f'//XCUIElementTypeOther[@name="{user.full_number}"]').click()
        self.find_element_by_accessibility_id('Send invitation').click()
        self.find_element_by_accessibility_id('Athletes invited!').is_displayed()
        self.click__ok()

        # check result
        assert 'upd' in self.find_element_by_xpath('//XCUIElementTypeTextField').text

    def click__create_game(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="leaguesSheetLeagueButton"])[3]').click()

    def add_game_title(self):
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypeOther[@name="Add game title"]'),
                       data=self.dummy.gen_string())

    def add_location_minsk(self):
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypeOther[@name="Add Location"]/XCUIElementTypeTextField'),
                       data='Minsk')
        self.find_element_by_xpath('//XCUIElementTypeOther[@name="Minsk, Belarus"]').click()

    def add_location_moscow(self):
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypeOther[@name="Add Location"]'),
                       data='Moscow')
        self.find_element_by_xpath('//XCUIElementTypeOther[@name="Moscow, Russia"]').click()

    def add_teams_to_game(self, team_names: list):
        self.find_element_by_xpath('//XCUIElementTypeOther[@name=" Add teams "]').click()
        self.send_keys(el=self.find_element_by_xpath(
            '(//XCUIElementTypeOther[@name="Search for a team or add new"])[3]'),
                       data=self.dummy.FILTER_KEY)
        self.find_element_by_accessibility_id(team_names[0]).click()
        if len(team_names) > 1:
            self.send_keys(
                el=self.find_element_by_xpath('(//XCUIElementTypeOther[@name="Search for a team or add new"])[3]'),
                data=self.dummy.FILTER_KEY)
            self.find_element_by_accessibility_id(team_names[1]).click()

    def add_officials_to_game(self, user):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name=" Officials (optional) "])[2]').click()
        self.send_keys(el=self.find_element_by_accessibility_id('Phone number, name, or add from contacts'),
                       data=user.number)
        self.find_element_by_accessibility_id(user.full_number).click()

    def click__schedule(self):
        self.find_element_by_accessibility_id('Schedule').click()
        self.find_element_by_accessibility_id('Game saved').is_displayed()

    def click__draft(self):
        self.find_element_by_accessibility_id('Draft').click()
        self.find_element_by_accessibility_id('Game saved in Draft state').is_displayed()

    def select_practice_type(self):
        self.find_element_by_accessibility_id('Practice').click()

    def add_practice_title(self):
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypeOther[@name="Add practice title"]'),
                       data=self.dummy.gen_string())

    def add_team_to_practice(self, team_name):
        self.send_keys(el=self.find_element_by_xpath('//XCUIElementTypeOther[@name="Search for a team or add new"]'),
                       data=self.dummy.FILTER_KEY)
        self.find_element_by_accessibility_id(team_name).click()

    def select_game(self):
        els = self.find_elements_by_xpath(
            '//XCUIElementTypeOther[contains(@name, "TA1") and contains(@name, "TA2")]')
        if not els:
            pytest.skip("There are no games created with names TA1 and TA2. Please run tests for creating games.")
        els[-1].click()

    def select_practice(self):
        els = self.find_elements_by_xpath(
            '//XCUIElementTypeOther[contains(@name, "PRACTICE")]')
        if not els:
            pytest.skip("There are no practice created. Please run tests for creating practices.")
        els[-1].click()

    def click__edit(self):
        self.find_element_by_xpath('//XCUIElementTypeOther[@name="Edit"]').click()

    def edit_location(self):
        el = self.find_element_by_xpath('//XCUIElementTypeOther[@name=""]//XCUIElementTypeTextField')
        el.click()
        el.clear()
        self.add_location_moscow()

    def edit_teams_for_game(self):
        self.find_element_by_xpath('//*[@name=" Add teams "]').click()
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="1"])[1]').click()
        self.find_element_by_xpath(
            '(//XCUIElementTypeOther[@name="1"])[1]/XCUIElementTypeOther[1]//XCUIElementTypeOther[2]').click()
        self.send_keys(el=self.find_element_by_xpath(
            '(//XCUIElementTypeOther[@name="Search for a team or add new"])[3]'),
            data=self.dummy.FILTER_KEY)
        self.find_element_by_accessibility_id(self.dummy.TEAM_NAME_2).click()

        self.find_element_by_xpath('(//XCUIElementTypeOther[@name="2"])[1]').click()
        self.find_element_by_xpath(
            '(//XCUIElementTypeOther[@name="2"])[1]/XCUIElementTypeOther[1]//XCUIElementTypeOther[2]').click()
        self.send_keys(el=self.find_element_by_xpath(
            '(//XCUIElementTypeOther[@name="Search for a team or add new"])[3]'),
            data=self.dummy.FILTER_KEY)
        self.find_element_by_accessibility_id(self.dummy.TEAM_NAME_1).click()

    def edit_team_for_practice(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name=""])[1]').click()
        self.find_element_by_xpath(
            '(//XCUIElementTypeOther[@name=""])[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]').click()
        self.send_keys(el=self.find_element_by_xpath(
            '(//XCUIElementTypeOther[@name="Search for a team or add new"])[2]'),
            data=self.dummy.FILTER_KEY)
        self.find_element_by_accessibility_id(self.dummy.TEAM_NAME_2).click()

    def edit_officials(self):
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name=" Officials (optional) "])[2]').click()
        self.find_element_by_xpath('//XCUIElementTypeStaticText[@name=""]').click()

    def click__delete_game(self):
        self.find_element_by_accessibility_id('Delete game').click()

    def click__delete_practice(self):
        self.find_element_by_accessibility_id('Delete practice').click()

    def click__yes_delete(self):
        self.find_element_by_accessibility_id('Yes, delete').click()

    def update_attendance(self):
        self.find_element_by_accessibility_id('Attendance ').click()
        self.find_element_by_xpath('//XCUIElementTypeOther[@name="1 TA1 0 RSVPs "]').click()
        self.find_element_by_accessibility_id('Here').click()
        self.find_element_by_xpath('//XCUIElementTypeOther[@name="1 TA2 0 RSVPs "]').click()
        self.find_element_by_accessibility_id('Absent').click()
        self.find_element_by_accessibility_id('Save attendance').click()

    def update_scores(self):
        self.find_element_by_accessibility_id('Scores ').click()
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name=""])[1]').click()
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name=""])[2]').click()

        self.find_element_by_xpath('//XCUIElementTypeOther[@name="1 TA1 0 POINTS "]').click()
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name=""])[2]').click()
        self.find_element_by_xpath('(//XCUIElementTypeOther[@name=""])[3]').click()

        self.find_element_by_accessibility_id('Save scores')
