public static void main(String[] args) {
        System.out.println("\t        PJ   \tPG   \tPE   \tPP   \tGA   \tGC   \tDG  \tPuntos");
        String titulo[]={"\nEquipo 3", "\nEquipo 1", "\nEquipo 4", "\nEquipo 5", "\nEquipo 6", "\nEquipo 2"};
        int valores[][]={
                {5,5,0,0,18,2,16,0},
                {5,3,1,1,16,7,9,0},
                {5,2,1,2,12,10,2,0},
                {5,2,1,2,11,11,0,0},
                {5,1,1,3,12,12,-7,0},
                {5,0,0,5,23,23,-20,0}
        };
        int PG3= valores[0][1];
        int PE3= valores[0][2];
        int puntos3=(PG3*2)+PE3;
        valores[0][7]=puntos3;

        int PG1= valores[1][1];
        int PE1= valores[1][2];
        int puntos1=(PG1*2)+PE1;
        valores[1][7]=puntos1;

        int PG4= valores[2][1];
        int PE4= valores[2][2];
        int puntos4=(PG4*2)+PE4;
        valores[2][7]=puntos4;

        int PG5= valores[3][1];
        int PE5= valores[3][2];
        int puntos5=(PG5*2)+PE5;
        valores[3][7]=puntos5;

        int PG6= valores[4][1];
        int PE6= valores[4][2];
        int puntos6=(PG6*2)+PE6;
        valores[4][7]=puntos6;

        int PG2= valores[5][1];
        int PE2= valores[5][2];
        int puntos2=(PG2*2)+PE2;
        valores[5][7]=puntos2;

        display(valores, titulo);


    }
    public static void display(int x[][], String titulo[]){

        for (int fila=0;fila<x.length;fila++){
            System.out.print(titulo[fila]+"\t");
            for (int columna=0;columna<x[fila].length;columna++){
                System.out.print(x[fila][columna]+"\t\t");
            }
            System.out.println();
        }
    }
