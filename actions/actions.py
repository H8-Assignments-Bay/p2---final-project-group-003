# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
    UserUtteranceReverted,
)


class ActionProjectChooser(Action):
    """Lists the contents of then known_recipients slot"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_project_chooser"

    async def run(
            self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
        ) -> List[EventType]:
        """Executes the custom action"""

        project_list = tracker.get_slot("PROJECT_LIST")
        project_code_list = [project['name'] for project in project_list]

        buttons = []
        for num, project_code in enumerate(project_code_list):
            title = project_code
            payload = f'inform{{"PROJECT_CODE": "{project_code}"}}'
            buttons.append({"title": title, "payload": payload})

        dispatcher.utter_message(
            response="utter_ask_invest_form_PROJECT_CODE",
            buttons=buttons,
        )
        events = []

        return events


class ActionShowProjects(Action):
    """Lists the contents of then known_recipients slot"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_show_projects"

    async def run(
            self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
        ) -> List[EventType]:
        """Executes the custom action"""

        project_list = tracker.get_slot("PROJECT_LIST")
        currency = tracker.get_slot("currency")

        project_formatted_list = []
        for num, project in enumerate(project_list):
            project_formatted_list.append(
                f"{50 * '-'}\n" \
                + f"{project['name']}\n" \
                + f"Tujuan peminjaman: {project['tujuan']}\n" \
                + f"Bunga: {project['rate']} | Durasi pinjaman: {project['durasi_pinjaman']}\n" \
                + f"Total pinjaman: {currency}{project['total_pinjaman']:,}\n" \
                + f"Slot pendanaan: {currency}{project['slot_pendanaan']:,}\n" \
                + f"Sisa waktu pendanaan: {project['sisa_waktu_pendananaan']}\n" \
                + "\n"
            )

        project_formatted_all = ''
        for project_formatted in project_formatted_list:
            project_formatted_all += project_formatted

        dispatcher.utter_message(
            response="utter_show_projects",
            formatted_projects=f"{project_formatted_all}"
        )
        events = []

        return events


class ActionInvest(Action):
    """Invest in project."""
    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_invest"

    async def run(
            self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
        ) -> List[EventType]:
        """Executes the custom action"""

        current_account_balance = int(tracker.get_slot("account_balance"))

        invest_amount = int(tracker.get_slot("amount_of_money"))

        dispatcher.utter_message(
            response="utter_invest_success",
            invest_amount=f"{invest_amount:,}",
        )

        # update slot account balance and withdrawal amount
        return [
            SlotSet("account_balance", current_account_balance - invest_amount),
            SlotSet("PROJECT_CODE", None),
            SlotSet("amount_of_money", None),
        ]


class ValidateInvestForm(FormValidationAction):
    """Validates Slots of the invest_form"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "validate_invest_form"

    async def validate_PROJECT_CODE(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
        """Validate the value of the PROJECT_CODE slot."""

        project_code = slot_value.lower()

        project_list = tracker.get_slot("PROJECT_LIST")
        project_code_list = [project['name'].lower() for project in project_list]

        if project_code.lower() not in project_code_list:
            dispatcher.utter_message(
                response="utter_project_code_not_found",
                PROJECT_CODE=project_code.upper(),
            )
            return {"PROJECT_CODE": None}
        
        return {"PROJECT_CODE": slot_value}

    async def validate_amount_of_money(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
        """Validate the amount of money to withdraw"""

        current_account_balance = tracker.get_slot("account_balance")

        invest_amount = int(slot_value)

        if invest_amount > current_account_balance:
            dispatcher.utter_message(
                response="utter_withdrawal_insufficient_balance",
                invest_amount=f"{invest_amount:,}",
                account_balance=f"{current_account_balance:,}",
            )
            return {"amount_of_money": None}

        return {"amount_of_money": slot_value}


## COMPLETE
class ActionWithdrawal(Action):
    """Withdraw from wallet"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_withdrawal"

    async def run(
            self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
        ) -> List[EventType]:
        """Executes the custom action"""

        current_account_balance = int(tracker.get_slot("account_balance"))

        withdrawal_amount = int(tracker.get_slot("amount_of_money"))

        dispatcher.utter_message(
            response="utter_withdrawal_success",
            withdrawal_amount=f"{withdrawal_amount:,}",
        )

        # update slot account balance and withdrawal amount
        return [
            SlotSet("account_balance", current_account_balance - withdrawal_amount),
            SlotSet("amount_of_money", None),
        ]


class ValidateWithdrawalForm(FormValidationAction):
    """Validates Slots of the withdrawal_form"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "validate_withdrawal_form"

    async def validate_amount_of_money(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
        """Validate the amount of money to withdraw"""

        current_account_balance = tracker.get_slot("account_balance")

        withdrawal_amount = int(slot_value)

        if withdrawal_amount > current_account_balance:
            dispatcher.utter_message(
                response="utter_withdrawal_insufficient_balance",
                withdrawal_amount=f"{withdrawal_amount:,}",
                account_balance=f"{current_account_balance:,}",
            )
            return {"amount_of_money": None}

        return {"amount_of_money": slot_value}


class ActionShowBalance(Action):
    """Shows the balance of account"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_show_balance"

    def run(
            self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
        ) -> List[EventType]:
        """Executes the custom action"""

        # show bank account balance
        current_account_balance = tracker.get_slot("account_balance")
        dispatcher.utter_message(
            response="utter_account_balance",
            account_balance=f"{current_account_balance:,}",
        )

        events = []

        return events

