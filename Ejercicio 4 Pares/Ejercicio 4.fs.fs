// Your code here!
open System

[<EntryPoint>]
let main argv =

    let lista = [1..51]
    let pares = [for i in lista do if i%2=0 then yield i]
    printfn "La cantidad de pares es: %d" (pares.Length)
    printfn("Pares: %A") pares
    let impares = [for i in lista do if i%2=1 then yield i]
    printfn "La cantidad de impares es: %d" (impares.Length)
    printfn("Impares %A") impares
        
    Console.ReadKey() |>ignore
    0 // return an integer exit code

