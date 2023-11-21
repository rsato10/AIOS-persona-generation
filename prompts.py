from langchain.prompts import PromptTemplate

###
### PROMPTS
###

# template = """\
# On a scale from 1-10 I am a {input_1} about enjoying seeking help from friends when making decisions
# On a scale from 1-10 I am a {input_2} about how long it take a long time to choose their favorite snack
# On a scale from 1-10 I am a {input_3} about prefering to follow rules while playing games	
# On a scale from 1-10 I am a {input_4} about considering how their choices impact others		
# On a scale from 1-10 I am a {input_5} on thinking about potential outcomes of a certain choice	
# On a scale from 1-10 I am a {input_6} about prefering making decisions quickly or taking their time
# When choosing a book, on a scale from 1-10 I am a {input_7} on thinking about how fun it will be to read	
# On a scale from 1-10 I am a {input_8} about likeing to explore all options before making a choice
# On a scale from 1-10 I am a {input_9} about prefering creating a plan before deciding what to do	
# On a scale from 1-10 I am a {input_10} about thinking it's important to consider others' opinions before making a choice
# Based on these statements what job title best fits me?
# """

questionnaire_template = """\
What persona best fits the results of this questionnaire QUESTIONNAIRE:
Question:
On a scale from 1 to 10 how much does your Persona enjoy seeking help from friends when making decisions?	
RESPONSE: {input_1}
Question:
On a scale from 1 to 10 how long does your Persona to choose their favorite snack?	
RESPONSE: {input_2}
Question:
On a scale from 1 to 10 how much does your Persona like following rules while playing games?	
RESPONSE: {input_3}	
Question:
On a scale from 1 to 10 how much does your Persona care about affecting others? 		
RESPONSE: {input_4}
Question:
On a scale from 1 to 10 how much does your Persona think about potential outcomes of a certain choice?	
RESPONSE: {input_5}
Question:
On a scale from 1 to 10 how fast does your Persona prefer making decisions with 10 being the fastest?	
RESPONSE: {input_6}
Question:
On a scale from 1 to 10 how much does your Persona like to read?	
RESPONSE: {input_7}
Question:
On a scale from 1 to 10 how much does your Persona like to explore all options before making a choice?	
RESPONSE: {input_8}
Question:
On a scale from 1 to 10 how much does your Persona like creating a plan before deciding what to do?	
RESPONSE: {input_9}
Question:
On a scale from 1 to 10 how important does your Persona think it is to consider others opinions before making a choice?
RESPONSE: {input_10}
"""

persona_template = """\
What job title best fits this persona PERSONA: {persona}?
"""

###
### PROMPT TEMPLATES 
###

questionnaire_prompt_template = PromptTemplate(
    input_variables=["input_1", "input_2","input_3","input_4","input_5","input_6","input_7","input_8","input_9","input_10",],
    template=questionnaire_template
)   

persona_prompt_template = PromptTemplate(
    input_variables=["persona"],
    template=persona_template
)

