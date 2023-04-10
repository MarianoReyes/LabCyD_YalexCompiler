(* Ejemplo básico *)

let if = "if"
let else = "else"
let switch = "switch"
let case = "case"

rule tokens =
  if	{ print("IF\n") }
  | else	{ print("ELSE\n") }
  | switch	{ print("SWITCH\n") }
  | case	{ print("CASE\n") }

