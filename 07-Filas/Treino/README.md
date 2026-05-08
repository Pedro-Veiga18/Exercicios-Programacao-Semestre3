<h1>Enunciado dos Exercícios</h1>

<h2>Exercício 01 — Simular fila de atendimento</h2>
<p>Crie um programa que:</p>
<ul>
  <li>Receba uma lista de nomes</li>
  <li>Coloque todos os nomes em uma fila</li>
  <li>Atenda os dois primeiros elementos da fila</li>
  <li>Mostre quais elementos permaneceram na fila após os atendimentos</li>
</ul>

<h3>Caso de teste</h3>
<p><strong>Entrada</strong></p>
<pre>["Ana", "Bruno", "Carlos", "Daniel"]</pre>

<p><strong>Saída esperada</strong></p>
<pre>["Carlos", "Daniel"]</pre>

<hr>

<h2>Exercício 02 — Verificar o primeiro sem remover (fila)</h2>
<p>Crie uma função que:</p>
<ul>
  <li>Receba uma lista de números</li>
  <li>Coloque os valores em uma fila utilizando deque</li>
  <li>Retorne o elemento que será o próximo a sair da fila, sem removê-lo</li>
</ul>

<h3>Regras</h3>
<ul>
  <li>Não utilizar popleft()</li>
  <li>Apenas consultar o primeiro elemento da fila</li>
</ul>

<h3>Caso de teste</h3>
<p><strong>Entrada</strong></p>
<pre>[5, 10, 15, 20]</pre>

<p><strong>Saída esperada</strong></p>
<pre>5</pre>

<hr>

<h2>Exercício 03 — Alternar atendimento da fila</h2>
<p>Crie uma função que:</p>
<ul>
  <li>Receba uma lista de nomes</li>
  <li>Coloque todos os nomes em uma fila utilizando deque</li>
  <li>Atenda uma pessoa e mova a próxima para o final da fila</li>
  <li>Repita o processo até restar apenas uma pessoa</li>
  <li>Retorne o nome da pessoa restante</li>
</ul>

<h3>Regras</h3>
<ul>
  <li>Utilizar fila (deque)</li>
  <li>Remover sempre o primeiro elemento da fila (atendido)</li>
  <li>Mover o próximo elemento para o final da fila</li>
  <li>Continuar o processo até restar apenas um elemento</li>
</ul>

<h3>Caso de teste</h3>
<p><strong>Entrada</strong></p>
<pre>["Ana", "Bruno", "Carlos", "Daniel", "Eduardo"]</pre>

<p><strong>Saída esperada</strong></p>
<pre>Bruno</pre>
<hr>

<h2>Sobre</h2>
<p>Este material foi desenvolvido por Rafael Nascimento para fins educacionais, com foco no estudo de estruturas de dados.</p>

<h2>Autor</h2>

<p>
  <a href="https://github.com/tec-Rafael" style="color:#fff;">
<p>Rafael Nascimento<br></p>
  </a>
</p>

<h2>Licença</h2>
<p>Uso livre para fins acadêmicos e educacionais.</p>