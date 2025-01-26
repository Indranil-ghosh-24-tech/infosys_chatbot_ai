from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAnswerQuestion(Action):

    def name(self) -> Text:
        return "action_answer_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        question = tracker.latest_message.get("text")
        answer = f"You asked: {question}. I'll answer soon!"
        dispatcher.utter_message(text=answer)
        return []
