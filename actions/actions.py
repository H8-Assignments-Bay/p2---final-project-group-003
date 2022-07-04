# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
    UserUtteranceReverted,
)

account_balance = 1_000_000

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

    async def run(
            self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict
        ) -> List[EventType]:
        """Executes the custom action"""

        # show bank account balance
        account_balance = account_balance
        # amount = tracker.get_slot("amount_transferred")
        dispatcher.utter_message(
            response="utter_account_balance",
            init_account_balance=f"{account_balance:,}",
        )

        events = []
        # active_form_name = tracker.active_form.get("name")
        # if active_form_name:
        #     # keep the tracker clean for the predictions with form switch stories
        #     events.append(UserUtteranceReverted())
        #     # trigger utter_ask_{form}_AA_CONTINUE_FORM, by making it the requested_slot
        #     events.append(SlotSet("AA_CONTINUE_FORM", None))
        #     # avoid that bot goes in listen mode after UserUtteranceReverted
        #     events.append(FollowupAction(active_form_name))

        return events
