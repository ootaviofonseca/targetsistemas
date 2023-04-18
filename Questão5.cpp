#include <iostream>
#include <string>

using namespace std;

void inverte(string& entrada) {
    int n = entrada.length();//Descobre o tamaho da string para poder inverter cada posição
    for (int i = 0; i < n / 2; i++) { 
        char auxiliar = entrada[i];//o auxiliar recebe cada valor a ser invertido
        entrada[i] = entrada[n - i - 1];// muda o valor de posicao
        entrada[n - i - 1] = auxiliar;//inverte
    }
}

int main() {
    string entrada;
    cout << "Informe uma string: ";
    cin >> entrada;
    string nova = entrada;
    inverte(entrada);
    cout << nova << " vira " << entrada << endl;
    return 0;
}