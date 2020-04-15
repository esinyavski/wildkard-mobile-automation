"""
Automated tests for covering Core Scenarios
"""


def test_new_user_sign_up(base_config, driver, login):
    login.click__sign_up()
    login.authenticate(
        phone_number=base_config.main_phone.number,
        country=base_config.main_phone.country)
    login.fill_profile()
    login.create_league_soccer()
    login.go_to_organizing()


def test_existing_user_login(base_config, driver, login):
    login.click__log_in()
    login.authenticate(
        phone_number=base_config.main_phone.number,
        country=base_config.main_phone.country)
    login.click__login_on_profile()
    login.go_to_landing()


def test_create_team__logo_determined_by_app__add_athlete(driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.create_team(name=dummy.TEAM_NAME_1, athlete_name=dummy.MAIN_USER)


def test_create_team__uploaded_logo__add_athlete(driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.create_team(name=dummy.TEAM_NAME_2, athlete_name=dummy.MAIN_USER, upload_logo=True)


def test_create_team__no_athlete(driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.create_team(name=dummy.TEAM_NAME_3)


def test_edit_team__rename__add_athlete(driver, organizing, dummy):
    organizing.go_to_search()
    new_name = organizing.edit_team(name=dummy.TEAM_NAME_3, athlete_name=dummy.MAIN_USER)
    organizing.check_notification(
        message=f"Wildkard Update: You've been added to the {new_name} team "
                f"in {dummy.LEAGUE_NAME} by f{dummy.MAIN_USER}. You can view this team's upcoming schedule "
                "and chat with teammates! ")


def test_schedule_game__both_teams__location__official(driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.click__create_game()
    organizing.add_game_title()
    organizing.add_location_minsk()
    organizing.add_teams_to_game(team_names=[dummy.TEAM_NAME_1, dummy.TEAM_NAME_2])
    organizing.add_officials(athlete_name=dummy.MAIN_USER)
    organizing.click__schedule()
    organizing.check_notification(
        message=f"Wildkard Update: Your upcoming game ({dummy.TEAM_NAME_1} vs {dummy.TEAM_NAME_2}) is scheduled")


def test_draft_game__one_team__no_location__no_official(driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.click__create_game()
    organizing.add_game_title()
    organizing.add_teams_to_game(team_names=[dummy.TEAM_NAME_1])
    organizing.click__draft()


def test_schedule_practice__location(driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.click__create_game()
    organizing.select_practice_type()
    organizing.add_practice_title()
    organizing.add_location_minsk()
    organizing.add_team_to_practice(team_name=dummy.TEAM_NAME_1)
    organizing.click__schedule()
    organizing.check_notification(message="Wildkard Update: Your upcoming practice scheduled")


def test_draft_practice_no_location(driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.click__create_game()
    organizing.select_practice_type()
    organizing.add_practice_title()
    organizing.add_team_to_practice(team_name=dummy.TEAM_NAME_1)
    organizing.click__draft()


def test_edit_game(driver, organizing):
    organizing.go_to_games()
    organizing.select_game()
    organizing.click__edit()
    organizing.edit_location()
    organizing.edit_teams_for_game()
    organizing.click__schedule()
    organizing.check_notification(message='Wildkard Update: Your upcoming game')


def test_edit_practice(driver, organizing):
    organizing.go_to_games()
    organizing.select_practice()
    organizing.click__edit()
    organizing.edit_location()
    organizing.edit_team_for_practice()
    organizing.click__schedule()
    organizing.check_notification(message='Wildkard Update: Your upcoming practice')


def test_delete_game(driver, organizing):
    organizing.go_to_games()
    organizing.select_game()
    organizing.click__edit()
    organizing.click__delete_game()
    organizing.click__yes_delete()
    organizing.validate()


def test_delete_practice(driver, organizing):
    organizing.go_to_games()
    organizing.select_practice()
    organizing.click__edit()
    organizing.click__delete_practice()
    organizing.click__yes_delete()
    organizing.validate()


def test_update_game_attendance(driver, organizing):
    organizing.go_to_games()
    organizing.select_game()
    organizing.update_attendance()


def test_update_game_scores(driver, organizing):
    organizing.go_to_games()
    organizing.select_game()
    organizing.update_scores()

