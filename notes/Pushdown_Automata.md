# Pushdown Automata

Pushdown Automata is a finite automata with extra memory called stack. It can therefore recognise **_Context Free languages_**.

A PDA can be defined by :
__G = (Q, &Sigma;, &Gamma;, q0, Z, F, &delta;)__ <br/>
Q = set of all states <br/>
&Sigma; = Set of input symbols <br/>
&Gamma; = Set of pushdown symobls <br/>
q0 = Initial State <br/>
Z = Initial Pushdown symbols <br/>
F = Set of final states <br/>
&delta; = Transition function ( **Q X {&Sigma; &Union; &Epsilon;} X &Gamma; &rarr; Q X &Gamma;***) <br/>

**Instantaneous Description (ID)** : It is an informal notation of how a PDA "computes" a input string and makes a decision that string is accepted or rejected.

**ID = (q, w, &alpha;)** <br/>
q = Current state <br/>
w = Remaining input <br/>
&alpha; = Stack contents (top) <br/>

**Tornstile Notation**
A ⊢ sign is called a "Tornstile notation" and represents one move. <br/>
A ⊢* sign represents a sequence of moves. <br/>
<br/>
__(p, b, T) ⊢ (q, w, &alpha;)__ <br/>
This implies that while taking a transition from step _p_ to state _q_, the input symbol _b_ is consumed and the top of the stack _T_ is replaced with a new string _&alpha;_.


### Example 
A PDA for the languange L = {a<sup>n</sup>b<sup>n</sup> | n > 0 }.
