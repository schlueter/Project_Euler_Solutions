import qualified Data.Set as Set

main = do
    let set1 = Set.fromList [3, 6..1000]
    let set2 = Set.fromList [5, 10..1000]
    putStrLn(show(sum(Set.toList(Set.union set1 set2))))
