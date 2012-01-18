<h1>Monty Python Text Generator</h1>

<p>This project was part of my Data Compression class. The main idea is to use different Markov chains to analyse a data text and symbol probabilities to hence be able to generate a similar (but quite different!) text.</p>

<h2>What does it do?</h2>
<p>The first part consists in analysing the "Monty Python and the Holy Grail" script using Markov chains of order 10. (<a href="http://en.wikipedia.org/wiki/Markov_chain">more details on Markov chains</a>). Briefly, Markov chains are a mathematical object stating that the probability of an event depends on the k last events, whiwh is perfectly suitable for text modelling (and I believe it was the first goal of Markov). Indeed, the probability of the character 'e' is quite strong if the past is 'th'. The whole idea is to know "how long" should be this past.</p>

<p>The scripts <code>py/probabilities.py</code> and <code>py/probabilities_multi.py</code> will analyse the text (for each Markov order in the list k_list) and build matrices of empirical transition probability between a k-uple (the past) and a symbol</p>

<p>These two scripts perform EXACTLY the same operations and will give exact same results. However, <code>py/probabilities_multi.py</code> use the multiprocessing python library to decrease execution time. If you have a multi-core architecture, that's the script you want to use.</p>

<p>The script <code>py/random_texts.py</code> will use these matrices to generate symbols based on the previous ones.</p>

<h2>How to use them? </h2>

<pre>
$ python probabilities.py ../data/data.txt
</pre>

<pre>
$ python probabilities_multi.py ../data/data.txt
</pre>

<pre>
$ python random_text.py ../data/data.txt [output_size]
</pre>

<h2>Example</h2>
<p>For k = 5:</p>

<p>KING ARTHUR: Yes!<br/>
VILLAGER #3: A bit.<br/>
VILLAGER #1: You saw saw saw it, did you could<br/>
separate, and master that!<br/>
ARTHUR: Will you on Thursday.<br/>
CUSTOMER: What do you can you think kill your every<br/>
good people. It’s one.)<br/>
OTHER FRENCH GUARDS: [whisperin</p>

<p>for k = 10:</p>

<p>KING ARTHUR: Will you ask your master that Arthur from the behind you looked–<br/>
DENNIS: Oh, what a give-away. Did you hear that, eh?<br/>
By exploiting the workers! By ’anging on to outdated imperialist dogma which perpetuates the economic and social differences</p>

<p>When the context is large enough (k=10), the sentences begin to make sense (limited by the fact of the randomness, and by the fact that THIS IS MONTHY FREAKING PYTHON!)</p>

<h2>Why is the first script so slow?</h2>
<p>~95% of exec time is spent in the built-in str.count() method (cf entropia.prof file). This method being written in C and optimized, optimization techniques like using Cython/Shedskin do not apply.</p>

<p>However, a parallel/multiprocessing technique can apply very easily (script <code>py/probabilities_multi.py</p>). It lead to a nice x2.8 exec speed result on my QuadCore laptop.</p> 
