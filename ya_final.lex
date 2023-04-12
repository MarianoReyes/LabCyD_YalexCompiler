(* Archivo Final *)
(* A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z *)

let if = "if"
let else = "else"
let switch = "switch"
let case = "case"
let digito = "0|1|2|3|4|5|6|7|8|9"
let negativo = "-"
let punto = "."
let numero = "negativo?digito(digito)*"
let numero_hexadecimal = "digito(digito)*(a|b|c|d|e|f|A|B|C|D|E|F)"
let numero_flotante = "digito(digito)*(punto)digito(digito)*"
let igual = "="
let letra = "a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z"
let identificador = "letra(letra|digito)*"

rule tokens =
  if	{ print("if\n") }
  | else	{ print("else\n") }
  | switch	{ print("switch\n") }
  | case	{ print("case\n") }
  | identificador	{ print("identificador\n") }
  | digito			{ print("digito\n") }
  | letra			{ print("letra\n") }
  | punto			{ print("punto\n") }
  | numero			{ print("numero\n") }
  | numero_hexadecimal			{ print("numero_hexadecimal\n") }
  | numero_flotante			{ print("numero_flotante\n") }
  | negativo			{ print("negativo\n") }
  | igual			{ print("igual\n") }
