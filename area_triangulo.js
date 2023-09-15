
function calcularAreaTriangulo(base, altura) {
  return (base * altura) / 2;
}


const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Ingrese la base del triángulo: ', (base) => {
  readline.question('Ingrese la altura del triángulo: ', (altura) => {
    const area = calcularAreaTriangulo(parseFloat(base), parseFloat(altura));
    console.log(`El área del triángulo es: ${area}`);
    readline.close();
  });
});
