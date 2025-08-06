# In-Context Learning (ICL)

## Zero-Shot Example

```prompt
Message: The weather is amazing today!  
Sentiment: ?
```
---

## Few-Shot Examples
```prompt
Message: I can't believe I missed my flight!  
Sentiment: Negative  

Message: Just got promoted at work—so excited!  
Sentiment: Positive  

Message: The weather is amazing today!  
Sentiment: ?
```

---

## Output Format

```prompt
Message: I can't believe I missed my flight!  
Sentiment: Negative  

Message: Just got promoted at work—so excited!  
Sentiment: Positive  

Message: The weather is amazing today!  
Sentiment: ?  

Give a one-word response.  
```


---

```prompt
Message: I can't believe I missed my flight!  
Sentiment: Negative  

Message: Just got promoted at work—so excited!  
Sentiment: Positive  

Message: The weather is amazing today!  
Sentiment:  

Respond with either "Positive," "Negative," or "Neutral."  
```

---

## Few-Shot Example: Consistent Style  

```prompt
Your task is to answer in a consistent style.  

<student>: Teach me about kindness.  

<teacher>: A single act of kindness can create ripples of change.  
A smile can brighten a stranger’s day,  
and a simple "thank you" can make someone feel valued.  

<student>: Teach me about courage.  
```