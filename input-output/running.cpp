#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;
    map<string, int> m;

     for(int i = 0; i < callings.size(); i++){
        auto it = find(players.begin(), players.end(), callings[i]);
        if(it != players.end()){
            int index = distance(players.begin(), it);
            m.insert({ players[index], index-1 });
        };
     }

     for(const auto& pair: m){
        cout << pair.first << pair.second << endl;
     }


  
    return answer;
}