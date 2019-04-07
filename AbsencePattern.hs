import qualified Data.Map.Strict as DM
import Data.Map.Strict (Map)
import Data.List (isInfixOf)
import Data.Foldable (toList)

isBad :: String -> Bool
isBad hay = any (`isInfixOf` hay)
  ["aa", "ala", "all", "lal", "lla", "lll"]

step :: Map String Integer -> Map String Integer
step m =
    DM.mapKeysWith (+) (take 2) .
    DM.filterWithKey (const . not . isBad) .
    DM.unionsWith (+) $
    map (\l -> DM.mapKeysWith (+) (l:) m) "ola"

steps n = sum . DM.elems $ iterate step (DM.singleton "" 1) !! n

main = mapM_ (print . (\n -> (n, steps n))) [0 .. 20]
