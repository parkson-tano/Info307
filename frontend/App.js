import { StatusBar } from 'expo-status-bar';
import { Text, SafeAreaView, StyleSheet } from "react-native";
import Register from './src/components/Register';
export default function App() {
  return (
    <SafeAreaView>
      <Register />
      <StatusBar style="auto" />
    </SafeAreaView>
  );
}


