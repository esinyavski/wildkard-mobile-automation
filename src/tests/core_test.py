"""
Automated tests for covering Core Scenarios
"""

import pytest


def test_sign_up_as_new_user(base_config, driver, login):
    login.click__sign_up()
    login.authenticate(
        phone_number=base_config.main_phone.number,
        country=base_config.main_phone.country)
    login.fill_profile()
    login.click__sign_up_on_profile()


def test_login_as_existing_user(base_config, driver, login):
    login.click__log_in()
    login.authenticate(
        phone_number=base_config.main_phone.number,
        country=base_config.main_phone.country)
    login.fill_profile()
    login.click__login_on_profile()


def test_create_league(driver, landing, dummy):
    landing.click__league_menu()
    landing.click__create_new_league()
    landing.select_sport__soccer()
    landing.type_league_name(name=dummy.LEAGUE_NAME)
    landing.click__create_league()


def test_send_message_to_league_chat(driver, landing, dummy):
    landing.select_league_from_page(name=dummy.LEAGUE_NAME)
    landing.send_message_to_chat()


def test_send_gif_to_league_chat(driver, landing, dummy):
    landing.select_league_from_page(name=dummy.LEAGUE_NAME)
    landing.send_gif_to_chat()


@pytest.mark.skip("The test should be corrected due to changed app logic")
def test_add_official_to_league(base_config, driver, organizing, dummy):
    organizing.click__settings()
    organizing.add_official_to_league(user=base_config.main_phone)
    organizing.check_notification(
        message=f"Wildkard Update: You've been invited to join {dummy.LEAGUE_NAME} "
                f"by {base_config.main_phone.full_number}")


@pytest.mark.skip("The test should be corrected due to changed app logic")
def test_accept_invitation_after_adding_official_to_team(driver, landing, dummy):
    landing.go_to_notification()
    landing.accept_invitation()
    landing.check_notification(message="You've accepted the invitation")


def test_create_team__default_logo__add_user(base_config, driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.create_team(name=dummy.TEAM_NAME_1,
                           user=base_config.main_phone)
    # The step below should be updated due to changing app logic
    # organizing.check_notification(
    #     message=f"Wildkard Update: You've been invited to join {dummy.LEAGUE_NAME} "
    #             f"by {base_config.main_phone.full_number}")


@pytest.mark.skip("The test should be corrected due to changed app logic")
def test_accept_invitation_after_creating_team(driver, landing, dummy):
    landing.go_to_notification()
    landing.accept_invitation()
    landing.check_notification(
        message="You've accepted the invitation")
    landing.go_to_dashboard()
    landing.check_team_displayed(name=dummy.TEAM_NAME_1)


def test_create_team__upload_logo__add_user(base_config, driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.create_team(name=dummy.TEAM_NAME_2,
                           user=base_config.main_phone,
                           upload_logo=True)
    # The step below should be updated due to changing app logic
    # organizing.check_notification(
    #     message=f"Wildkard Update: You've been invited to join {dummy.LEAGUE_NAME} "
    #             f"by {base_config.main_phone.full_number}")


def test_create_team__no_user(driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.create_team(name=dummy.TEAM_NAME_3)


def test_edit_team__rename__add_user(base_config, driver, organizing, dummy):
    organizing.go_to_search()
    organizing.edit_team(name=dummy.TEAM_NAME_3, user=base_config.main_phone)
    # The step below should be updated due to changing app logic
    # organizing.check_notification(
    #     message=f"Wildkard Update: You've been invited to join {dummy.LEAGUE_NAME} "
    #             f"by {base_config.main_phone.full_number}")


@pytest.mark.skip("The test should be corrected due to changed app logic")
def test_accept_invitation_after_editing_team(driver, landing, dummy):
    landing.go_to_notification()
    landing.accept_invitation()
    landing.check_notification(message="You've accepted the invitation")


def test_send_message_to_team_chat(driver, landing, dummy):
    landing.select_team_from_page(name=dummy.TEAM_NAME_1)
    landing.send_message_to_chat()


def test_send_gif_to_team_chat(driver, landing, dummy):
    landing.select_team_from_page(name=dummy.TEAM_NAME_1)
    landing.send_gif_to_chat()


def test_schedule_game__both_teams__location__official(base_config, driver, organizing, dummy):
    organizing.go_to_create_menu()
    organizing.click__create_game()
    organizing.add_game_title()
    organizing.add_location_minsk()
    organizing.add_teams_to_game(team_names=[dummy.TEAM_NAME_1, dummy.TEAM_NAME_2])
    organizing.add_officials_to_game(user=base_config.main_phone)
    organizing.click__schedule()
    organizing.check_notification(
        message=f"Wildkard Update: Your upcoming game ({dummy.TEAM_NAME_1} vs {dummy.TEAM_NAME_2}) is scheduled")


def test_update_game_attendance(driver, organizing):
    organizing.go_to_games()
    organizing.select_game()
    organizing.update_attendance()


def test_update_game_scores(driver, organizing):
    organizing.go_to_games()
    organizing.select_game()
    organizing.update_scores()


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
    organizing.check_notification(message="Wildkard Update: Your upcoming practice is scheduled")


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
    organizing.check_notification(
        message='Wildkard Update: Your upcoming game')


def test_edit_practice(driver, organizing):
    organizing.go_to_games()
    organizing.select_practice()
    organizing.click__edit()
    organizing.edit_location()
    organizing.edit_team_for_practice()
    organizing.click__schedule()
    organizing.check_notification(
        message='Wildkard Update: Your upcoming practice')


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
