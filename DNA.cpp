#include <iostream>
#include <string>
#include <list>
using namespace std;


void split_3 (string cadena)
{
    //list <string> aminoacidos;
    int longitud = cadena.size();
    char tripleta [3]={'A','B','C'}; 

        int i,j = 0;
        for (int i=0;i<longitud;i++){
            for (int j=0;;j++){
                {
                    tripleta[j] = cadena[i];
                    if(j%2==0)
                    {
                        j=0;
                    }                
                }
        }
            
        if(j==3)
            j=0;
           
       
        cout << tripleta[0];
    }
    //tripleta[0]=cadena[1];
    //cout << tripleta[0]<< endl;
}


int main()
{
    
    string cadena = "ATGGAAGTATTTAAAGCGCCACCTATTGGGATATAAG";
    //MEVFKAPPIGI
    split_3(cadena);

}

