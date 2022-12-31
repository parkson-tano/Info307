import { View, Text, SafeAreaView } from "react-native";
import React from 'react'
import Balance from "./dashboard/Balance";
import Features from "./dashboard/Features";
const Dashboard = () => {
  return (
    <SafeAreaView>
          <View>
      <Text>My Dashboard</Text>
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