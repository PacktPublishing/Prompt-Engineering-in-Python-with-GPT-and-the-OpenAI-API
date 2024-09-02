#We are using the backoff package to handle the rate limit error
## We wrap the openai.ChatCompletion.create() in our own function 
### and use the @backoff.on_exception() decorator.
import backoff

@backoff.on_exception(backoff.expo, openai.RateLimitError)
def query_llm_single_turn(prompt, model="gpt-3.5-turbo", temperature=0, **kwargs):
    """
    This function queries the openai ChatCompletion API, with exponential backoff.
    
    Args:
        prompt(str): The prompt  
        model(str): The type of model to use. The default is "gpt-3.5-turbo".
        temperature(float): The temperature to use. The default is 0.
        **kwargs: Additional keyword arguments to be passed to openai.ChatCompletion.create()
    Returns:
        An opanai ChatCompletion object.
    """
    ##Set up the messages list
    messages = [{"role": "user", "content": prompt}]
    return openai.chat.completions.create(
        model=model,    
        messages=messages,
        temperature=temperature,
        **kwargs)

#Copyright Slava Razbash and AI Upskill (aiupskill.io)
