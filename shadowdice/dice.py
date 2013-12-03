from random import randint
import json

class Result(object):
    def __init__(self, rolls, limit=-1, edged=False):
        self.edged = edged
        self.limit = limit if limit > 0 and not edged else len(rolls)
    
        self.rolls = list(sorted(rolls, reverse=True))
        
        self.sixes = self.rolls.count(6)
        self.successes = min(self.sixes + self.rolls.count(5), self.limit)
        self.ones = self.rolls.count(1)
        self.glitch = self.ones > (len(self.rolls) // 2)
    
    def __repr__(self):
        return json.dumps({"successes": self.successes, "glitch": self.glitch,
            "rolls": self.rolls})
            
    def __add__(self, other):
        return Result(self.rolls + other.rolls, limit=min(self.limit, other.limit),
            edged=max(self.edged, other.edged))
        

class Dice(object):
    def __init__(self, n = 0, edge = 0, limit = -1):
        self.n = n
        self.edge = edge
        self.limit = limit
        
    def __call__(self):
        result = Result([randint(1,6) for x in range(self.n + self.edge)],
            edged=self.edge > 0, limit=self.limit)
        
        if self.edge > 0 and result.sixes > 0:
            result += Dice(edge=result.sixes)().result
        
        return DiceResult(self, result)
    def __repr__(self):
        result = "Dice(n={}".format(self.n)
        
        if self.edge > 0:
            result += ", edge={}".format(self.edge)
            
        if self.limit > -1:
            result += ", limit={}".format(self.limit)
        
        result += ")"
    
        return result

class DiceResult(object):
    def __init__(self, dice, result):
        self.dice = dice
        self.result = result
    
    def __repr__(self):
        return "{} = {}".format(self.dice, self.result)

