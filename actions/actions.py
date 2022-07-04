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

projects_list = {
    "project_1": {
        "name": "REG506-AMD001",
        "total_pinjaman": 100_000_000,
        "slot_pendanaan": 57_500_000,
        "sisa_waktu_pendananaan": "2 hari lagi",
        "grade": "A",
        "rate": "14%",
        "durasi_pinjaman": "4 bulan",
        "tujuan": "invoice financing",
    },
    "project_2": {
        "name": "REG507-NVD005",
        "total_pinjaman": 100_000_000,
        "slot_pendanaan": 71_700_000,
        "sisa_waktu_pendananaan": "1 hari lagi",
        "grade": "C",
        "rate": "18%",
        "durasi_pinjaman": "4 bulan",
        "tujuan": "invoice financing",
    },
    "project_3": {
        "name": "REG508-INT023",
        "total_pinjaman": 70_000_000,
        "slot_pendanaan": 38_500_000,
        "sisa_waktu_pendananaan": "3 hari lagi",
        "grade": "C",
        "rate": "18%",
        "durasi_pinjaman": "3 bulan",
        "tujuan": "working capital financing",
    },
}


class ActionPayProject(Action):
    """Transfer to invest in project."""
    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_pay_project"

    async def run(
            self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
        ) -> List[EventType]:
        """Executes the custom action"""

        # slots = {
        #     "AA_CONTINUE_FORM": None,
        #     "zz_confirm_form": None,
        #     "PROJECT": None,
        # }
        pass


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


class ActionWithdraw(Action):
    """Withdraw from wallet"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_withdrawal"

    async def run(
            self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
        ) -> List[EventType]:
        """Executes the custom action"""

        current_account_balance = tracker.get_slot("account_balance")

        withdrawal_amount = int(tracker.get_slot("withdrawal_amount"))

        dispatcher.utter_message(
            response="utter_withdrawal_amount_validated",
            withdrawal_amount = withdrawal_amount
        )

        # update slot account balance and withdrawal amount
        return [
            SlotSet("account_balance", current_account_balance - withdrawal_amount),
            SlotSet("withdrawal_amount", None),
        ]


class ValidateWithdrawalForm(FormValidationAction):
    """Validates Slots of the withdrawal_form"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "validate_withdrawal_form"

    async def validate_withdrawal_amount(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
        ) -> Dict[Text, Any]:
        """Validate the amount of money to withdraw"""

        account_balance = tracker.get_slot("account_balance")

        withdrawal_amount = int(slot_value)

        if withdrawal_amount > account_balance:
            dispatcher.utter_message(
                response="utter_insufficient_balance",
            )
            return {"withdrawal_amount": None}

        return {"withdrawal_amount": slot_value}
