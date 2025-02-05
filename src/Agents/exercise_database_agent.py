import crewai as crewai
from textwrap import dedent
from src.Agents.base_agent import BaseAgent


class ExerciseDataBaseAgent(BaseAgent):
    role: str
    goal: str
    backstory: str

    def __init__(self, **kwargs):
        role = """
            You are the Exercise Database Agent.
            """
    
        goal = """
            Recommend exercises from your database for the conditioning coach to design a workout routine. 
            """

        backstory = """
            You are an expert in exercise science. You manage a large database of exercises. You give science-based
            recommendations tailored to the individual's goals. 
            """
    
        super().__init__(
            role = kwargs.pop('role', role),
            goal = kwargs.pop('goal', goal),
            backstory = kwargs.pop('backstory', backstory),
            tools=[],
            **kwargs
        )

    def recommend_exercises(self):
        # Preprocessing goes here
        return crewai.Task(
            description=dedent(f"""
                Recommend exercises based on sport, fitness level, and goals.
            """),
            agent=self,
            expected_output="A bulleted list of exercises."
        )        