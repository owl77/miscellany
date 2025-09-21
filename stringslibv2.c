#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int dim(char ** list);

int equals(char ** a , char ** b ){
if(dim(a)==dim(b)){
int size = dim(a);
for(int i = 0; i < size; i++){
if(a[i]!=b[i]){return -1;}}
return 0;}return -1;}

int dim(char ** list){
int i = 0;
while(list[i]!=NULL){i++;}
return i;}

/* get maximum size of string elements for better malloc  */

int bytedim(char ** list){


int d = dim(list);
if(d == 0){return 0;}
int l = strlen(list[0]);
for(int i = 1; i < d; i++){
if (strlen(list[i]) > l){l = strlen(list[i]);}
}

return l;
}




char **slice(char ** list, int start, int end){
char ** out = (char **)malloc(dim(list)*sizeof(char *)+1 );
if (start==end){
out[0] =NULL; return out;	
	
	
}
int j = 0;for(int i = start; i < end; i++){
out[j] = malloc(bytedim(list)*sizeof(char)+1);
out[j]= list[i];
j++;} out[j]=NULL; return out;}

char ** singleton(char* sing){
int l = strlen(sing);
char ** out = (char **)malloc(l*sizeof(char *) + 1);
/*8 or sizeof a pointer 64-bit machines */
out[0] = sing;
out[1] = NULL;
return out;}

char **push(char ** list, char* element){
if(list ==NULL){return singleton(element);}

int ins = dim(list); char ** out = slice(list,0,ins);
out[ins]= element;out[ins+1] = NULL;return out;}

char ** invert(char ** list){
if(list==NULL){return NULL;}

int ins = dim(list);
char ** out = slice(list,0,ins);
for(int j = 0; j < ins; j++){
out[ins-j-1] = list[j];
}
out[ins] =NULL;
return out;}

void display(char ** list){
int size = dim(list);printf("{ ");
for(int i = 0; i < size-1; i++){printf("\"%s\", ",list[i]);
}printf("\"%s\" }\n",list[size-1]);}

int includes(char ** list, char *element){
int size = dim(list);for(int i = 0; i < size; i++){
if(strcmp(list[i],element)==0){return 0;}
}return -1;}

int count(char * string, char e){
int l = strlen(string);
int count = 0;
for(int i = 0; i < l; i++){
if(string[i]==e){count++;}
}return count;}

char * stringslice(char * string,int start,int end){
int d = end-start;char * out = (char *)malloc(d*sizeof(char)+1);
int j = 0;for(int i = start; i < end; i++){
out[j]=string[i]; j++;
}out[j]='\0';return out;}

int firstindex(char *string, char mark){
int l = strlen(string); 
for(int i = 0; i < l; i++){
if(string[i]==mark){return i;}
}return -1;}

char ** split(char * string, char mark){

int ind = firstindex(string,mark);
int len = strlen(string);
if(ind==-1){return singleton(string);}
char * seg = stringslice(string,0,ind);
char * seg2 = stringslice(string,ind+1,len);
/* char ** out = (char **)malloc(sizeof(string)*16);*/
char ** out = (char **)malloc(len * sizeof(char *) + 1);
out = split(seg2,mark);
return push(out,seg);}

	
/*real split = split + invert */

char * join(char* a, char* b){
int siz = strlen(a) + strlen(b);
char * out = (char *)malloc(siz*sizeof(char)+1);
for(int i= 0; i < strlen(a); i++){
out[i] = a[i];
}
for(int i =0 ; i < strlen(b); i++){

out[strlen(a)+i] = b[i];}
out[siz]='\0';

return out;
}


char* onesub(char*  string, char*  from, char* to )
{ 
int len = strlen(string);
int si = strlen(from);
int tt = strlen(to);
for(int i = 0; i < len-si+1; i++){ 
if(strcmp(stringslice(string,i,i+si), from)==0){
char * out1 = (char *)malloc(len*sizeof(char) +tt*sizeof(char)) ;	
char * out2 = (char *)malloc(len*sizeof(char) +tt*sizeof(char));
out1 = join(stringslice(string,0,i),to);
out2 = join(out1, stringslice(string,i+si,len));
return out2;} }return string;}

char* sub(char * string, char * from, char * to)

{
	
int len = strlen(string);
int si = strlen(from);
int tt = strlen(to);
for(int i = 0; i < len-si+1; i++){
if(strcmp(stringslice(string,i,i+si), from)==0){
	char * out1 = (char *)malloc(len*sizeof(char) +tt*sizeof(char)) ;	
	char * out2 = (char *)malloc(tt*len*sizeof(char));
	
	
out1 = join(stringslice(string,0,i),to);
out2 = join(out1, sub(stringslice(string,i+si,len),from,to));
free(out1);
return out2;} }return string;}


char* predicates[200] = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O", "P","Q","R","S","T","U","V","W","X","Y","Z", NULL};
char* variables[200] = {"x","y","z","u","v","w","s","t",NULL};
char * constants[200] = {"a","b","c","d","e","f",NULL};


int formparse(char** string);
int thatterm(char** string);

int body(char** string){
	if(thatterm(string)==0){return 0;}
	if(dim(string)==0){return -1;}
	if(includes(constants,string[0])==0 || includes(variables,string[0])==0){
		if(dim(string)==1){return 0;}
	    if(dim(string)>2){
		   if( strcmp(string[1],",")==0 && body(slice(string,2,dim(string))) == 0){return 0;}
	   }
}

if(dim(string)>8){		
for(int i = 6; i < dim(string); i++){
	
if(thatterm(slice(string,0,i) )==0 && strcmp(string[i],",")==0){return body(slice(string,i+1,dim(string)));}	
}}	
	
	return -1;
}

int thatterm(char ** string);


int varbody(char** string){

	if(dim(string)==0){return -1;}
	if(dim(string)==1){if( includes(variables,string[0])==0){return 0;}}
	if(dim(string)>2){
    if(strcmp(string[1],",")==0  && varbody(slice(string,2,dim(string))) == 0){return 0;}
	
	if(dim(string)> 6){
		for(int i = 6; i < dim(string); i++){
			
			if(thatterm(slice(string,0,i))==0 && strcmp(string[i],",")==0  && slice(string,i,dim(string)) == 0){return 0;}
		
		}
			
		}
		
		
	}
	
	
	
	
	return -1;}




          
          
int parseatomic(char **string)
	{
		
if( dim(string) > 2 && includes(predicates, string[0])==0
		
&& strcmp(string[1],"(")==0 &&strcmp(string[dim(string)-1],")")==0 &&

 body(slice(string, 2, dim(string)-1 ))==0  	)
	 
	 {return 0;}
   return -1;
}



int existsparse(char **string){
    if(dim(string) ==0){return -1;};
 if(strcmp(string[0],"exists")==0 && varbody(slice(string, 1, dim(string)-1)) == 0
	 && strcmp(string[dim(string)-1],".")==0){return 0;}

return -1;}



int thatparse(char **string){
  
	if(dim(string)==2 && strcmp(string[0],"that")==0 && strcmp(string[1],".")==0 ){return 0;}
 if(strcmp(string[0],"that")==0 && varbody(slice(string, 1, dim(string)-1)) == 0
	 && strcmp(string[dim(string)-1],".")==0){return 0;}

return -1;}

int thatterm(char **string){
if(dim(string)<5){return -1;}	
for(int i= 2; i < dim(string)-2; i++){
if(thatparse(slice(string,0,i) )==0 && formparse(slice(string,i,dim(string)))==0 ){return 0;}	
}	
return -1;	
}


int formparse(char ** string);

int existsformula(char **string){
if(dim(string)<7){return -1;}	
for(int i = 3; i < dim(string)-3;i++){
if(existsparse(slice(string,0,i))==0 && formparse(slice(string,i,dim(string)) )==0){return 0;} }

return -1;}


int assandformula(char** string){

if(dim(string)<9){return -1;}	
		
    for(int i = 4; i< dim(string)-4; i++)
	
	{	
	 if( formparse(slice(string,0,i))==0 && strcmp(string[i],"and")==0 &&
		(   formparse(slice(string,i+1,dim(string)) )==0 || assandformula(slice(string,i+1,dim(string)) )==0    )
				 ) {return 0;}}return -1;}






int andformula(char** string){

if(dim(string)<11){return -1;}	
		
    for(int i = 4; i< dim(string)-5; i++){	
	 if( formparse(slice(string,1,i))==0 && strcmp(string[i],"and")==0 && strcmp(string[0],"(")==0
		  && strcmp(string[dim(string)-1],")")==0 && 
			  
			  ( formparse(slice(string,i+1,dim(string)-1))==0 
				  || assandformula(slice(string,i+1,dim(string)-1))==0)){return 0;}}return -1;}



int notformula(char** string){

	if(dim(string) <5){return -1;}
	if(strcmp(string[0],"not")==0 && formparse(slice(string,1,dim(string)))==0){return 0;}

if(strcmp(string[0],"not")==0 && strcmp(string[1],"(")==0 && strcmp(string[dim(string)-1],")")==0  )
{if(formparse(slice(string, 2, dim(string)-1))==0){return 0;}}	
	
return -1;	
}

int formparse(char ** string){
	
	if(parseatomic(string)==0){return 0;}
	
    if(notformula(string)==0){return 0;}
	
	if(andformula(string)==0){return 0;}
	
	if(existsformula(string)==0){return 0;}	
      
return -1;	
}




void load(char ** source, char * target[],int d){
for(int i = 0; i < d; i++){
target[i]=source[i];}
target[d]=NULL;

}





int main(){
	
	char str[12];
	for(int i =0 ; i<100; i++){
		
	sprintf(str,"%d",i);	
	variables[8+i]=join("x_",str);	
	constants[6+i]=join("c_",str);
	predicates[26+i]=join("P_",str);	
	}
	variables[108]=NULL;
    constants[106]=NULL;
	predicates[126]=NULL;
	
	
	char input[100]; 
	printf("Enter intensional logic expression to parse: \n");
	fgets(input, 100, stdin); 
	
	
	
	char * a = sub(input,"("," ( ");
	char * b = sub(a ,")"," ) ");
	char * c = sub(b, ","," , ");
	char * d = sub(c, "."," . ");
	
	while(strcmp(d,sub(d,"  "," "))!=0){d = sub(d,"  "," ");}
    if(d[0]==' '){d = stringslice(d,1,strlen(d));}
	printf("Pretty version : %s\n", d);
	char ** cc = invert(split(d,' '));

	
	display(slice(cc,0,dim(cc)-1));
	printf("Parsing result: %d \n", formparse(slice(cc,0,dim(cc)-1))); 
	
return 0;
}
