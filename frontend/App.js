import * as React from "react";
import { Button, View, Text } from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Register from "./src/components/Register";
import MomoRegister from "./src/components/MomoRegister";
import AgentRegister from "./src/components/AgentRegister";
// function DetailsScreen({ navigation }) {
//   return (
//     <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
//       <Text>Details Screen</Text>
//       <Button
//         title="Go to Details... again"
//         onPress={() => navigation.navigate("Details")}
//       />
//     </View>
//   );
// }

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={Register} />
        <Stack.Screen name="MomoRegister" component={MomoRegister} />
        <Stack.Screen name="AgentRegister" component={AgentRegister} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
