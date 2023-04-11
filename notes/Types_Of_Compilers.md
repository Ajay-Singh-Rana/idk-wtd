# Types Of Compilers

## Code Generation
- If we generate **real machine code**, we get an executable that the OS can load directly into the chip.
- Native code is lightening fast but is hard to generate and tied up to the architecture strongly.
- If we generate **bytecode**, these synthetic instructions are designed to map a little more colsely to the 
language's semantics and not be so tied to the pecularities of any one computer architecture.

## Virtual Machine
Since There is no chip that works with the bytecode we have to translate it. There are two ways of doing it:
1. Write a little mini-compiler for each target architecture that converts the bytecode to native code for that machine.
But we get to reuse the rest of the compiler pipeline across all of the machines.
2. A **VM (Virtual Machine)** a program that emulates a hypothetical chip supporting our virtual architecture at run time.
Running bytecode in VM is slower than translating it to native code ahead of time because every instruction must be simulated at run time 
each time it executes. This provides simplicity and portability.

### Runtime
If we compiled the code to machine code we simply tell the operating system to load the executable and off it goes.
If we compiled it to bytecode we need to start up the VM and load the program into that.

+ Services like **Garbage Collection** and support for tests are called runtime and are inserted directly into the executable.

## Single Pass Compilers
- These compilers interleave parsing, analysis and code generation so that they porduce output code directly in the parser, without ever allocating any syntax trees or other
Intermediate Representations.
- These restrict the design of the language.

### Syntax Directed Translation
It is a structured technique for building all-at-once compilers. An action is associated with each piece of grammar, usually one that generates output code.
Whenever the parser matches the chunk of synatx, it executes the action, building up the target code one rule at a time.

## Tree Walk Interpreters
- Some languages begin executing code right after passing it to an AST (with maybe a bit of static analysis applied). 
- To run the program the interpreter traverses the syntax tree one branch and leaf at a time, evaluating each node as it goes.
- These are suitable for little languages and tend to be slow.

## Transpilers
We write a front end for our language. Then, in the back-end, instead of doing all the work to lower the semantics to some primitive target language, we produce a string of valid source code for some other language that is about as high level as ours.
Now, we use the existing compilation tools for that language as an escape route.
- Also called **source-to-source** compiler or **transcompiler**.

## Just-In-Time Compilation
We load platform independent bytecode and tehn compile it to native code for the computer architecture.
- JIT compilers are a good way of implementing machine independent and dynamic compilers. But these are unable to work closely with the hardware.

## Compilers Versus Interpreters
- Compiling is an implementation technique that involves translating a source language to some other usually lower-level form.
- When a language implementation ***"is a compiler"***, it translates source code to some other form but doesn't execute it.
- Wehn an implementation ***"is an itnerpreter"*** it takes the source code and executes it immediately.

