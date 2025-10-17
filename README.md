<h1 align="center">🌠 Star Evolution Simulator</h1>
<p align="center"><em>Modeling stellar evolution stages using Python</em></p>

<hr>

<h2>🎯 Purpose & Scope</h2>
<p>
This project simulates <strong>stellar evolution</strong> from main sequence to late stages.
It calculates changes in luminosity, radius, and temperature based on stellar mass, 
using both theoretical and empirical models.
</p>

<ul>
  <li>Compute stellar lifetime for different masses.</li>
  <li>Simulate luminosity and temperature changes over time.</li>
  <li>Visualize evolution on the <strong>Hertzsprung–Russell (H–R) diagram</strong>.</li>
  <li>Supports bilingual outputs (Turkish / English).</li>
</ul>

<hr>

<h2>🧩 Project Structure</h2>
<pre>
📁 Star-Evolution-Simulator/
│
├── evolation.py     → Core evolution simulation in English
├── evrim.py         → Turkish version of the simulator
└── README.md        → This documentation
</pre>

<hr>

<h2>⚙️ Installation & Usage</h2>
<ol>
  <li>Install Python 3.x.</li>
  <li>Install required packages:
    <pre><code>pip install numpy matplotlib</code></pre>
  </li>
  <li>Run one of the scripts:
    <pre><code>python evolation.py
python evrim.py</code></pre>
  </li>
  <li>Plots showing stellar evolution will appear and can be saved as PNG images.</li>
</ol>

<hr>

<h2>🧮 Scientific Model</h2>
<p>
The simulator follows simplified analytic relationships from stellar physics:
</p>

<pre>
tₛ ≈ 10¹⁰ × (M / M☉)⁻²·⁵  years
</pre>

<p>
Where:
<ul>
  <li><code>M</code>: stellar mass</li>
  <li><code>M☉</code>: solar mass</li>
  <li><code>tₛ</code>: approximate stellar lifetime</li>
</ul>
This formula reflects how massive stars evolve faster than smaller ones.
</p>
