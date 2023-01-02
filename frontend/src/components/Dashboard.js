import { View, SafeAreaView } from "react-native";
import React from 'react'
import Balance from "./dashboard/Balance";
import Features from "./dashboard/Features";
import { Text } from "@rneui/themed";
const Dashboard = () => {
  return (
    <SafeAreaView>
      <View>
        <Text h4 style={{paddingHorizontal: 10, fontWeight: "bold", margin: 10, backgroundColor: 'white', width: "100%"}}>
          Main Account
        </Text>
      </View>
    <View>
      <Balance />
    </View>
    <View>
      <Features />
    </View>
    </SafeAreaView>
  )
}

export default Dashboard