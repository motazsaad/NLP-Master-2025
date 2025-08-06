# Chain of Thoughts CoT 

## initial prompt 
```prompt
15 of us want to go to a restaurant.
Two of them have cars
Each car can seat 5 people.
Two of us have motorcycles.
Each motorcycle can fit 2 people.

Can we all get to the restaurant by car or motorcycle?
```


--------------------

## instruct the model to think 

```prompt
15 of us want to go to a restaurant.
Two of them have cars
Each car can seat 5 people.
Two of us have motorcycles.
Each motorcycle can fit 2 people.

Can we all get to the restaurant by car or motorcycle?

Think step by step.
```


----------------------

## intruct the model to think and explain 

```prompt
15 of us want to go to a restaurant.
Two of them have cars
Each car can seat 5 people.
Two of us have motorcycles.
Each motorcycle can fit 2 people.

Can we all get to the restaurant by car or motorcycle?

Think step by step.
Explain each intermediate step.
Only when you are done with all your steps,
provide the answer based on your intermediate steps.
```


---- 

## asking the model to answer first, explain later 

```prompt
15 of us want to go to a restaurant.
Two of them have cars
Each car can seat 5 people.
Two of us have motorcycles.
Each motorcycle can fit 2 people.

Can we all get to the restaurant by car or motorcycle?

Think step by step.
Provide the answer as a single yes/no answer first.
Then explain each intermediate step.
```

------------------------

## mutiple steps prompt 

```prompt
Perform the following actions: 
1 - Summarize the following text delimited by triple 
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following 
keys: french_summary, num_names.

Separate your answers with line breaks.

Text:


```In a charming village, siblings Jack and Jill set out on  
a quest to fetch water from a hilltop  
well. As they climbed, singing joyfully, misfortune  
struck—Jack tripped on a stone and tumbled  
down the hill, with Jill following suit.  
Though slightly battered, the pair returned home to  
comforting embraces. Despite the mishap,  
their adventurous spirits remained undimmed, and they  
continued exploring with delight.```
```

