// Your code here!
open System

let multi a b = 
    let lista = [for i in 1..b -> a]
    let suma = List.sum lista
    printfn "La multiplicacion es:%d" suma
    


[<EntryPoint>]
let main argv =
    
    multi 10 12

    Console.ReadKey() |>ignore
    0 // return an integer exit code