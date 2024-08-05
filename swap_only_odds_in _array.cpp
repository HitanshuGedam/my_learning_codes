class Kata
{
public:
    std::vector<int> sortArray(std::vector<int> array)
    {
        for(int i = 0; i < array.size(); i++){
          for(int j = 0; j < array.size(); j++){
            if(array[i] % 2 != 0 && array[j] % 2 != 0 && array[i] < array[j]){
              int temp = array[i];
              array[i] = array[j];
              array[j] = temp;
            }
          }
        }
        return array;
    }
};
