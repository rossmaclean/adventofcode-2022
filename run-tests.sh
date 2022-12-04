set -eu


function runTests() {
  pwd=$(pwd)
  for d in ./challenges/*/ ; do
      echo "Running tests in $d"
      cd "$d" || exit
      python3 *_test.py
      cd "$pwd" || exec
  done
}

runTests