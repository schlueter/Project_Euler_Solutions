fib :: Int -> Int -> [Int]
fib 0 _ = []
fib m n = m : (fib n (m+n))

main = do
  putStrLn (show (sum (filter even (takeWhile (<4000000) (fib 1 1)))))
