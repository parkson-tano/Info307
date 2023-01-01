import { View, Text, TextInput, StyleSheet, SafeAreaView } from 'react-native'
import React, { useState } from 'react'
import axios from "axios";
import Icon from "react-native-vector-icons/FontAwesome";
import { Input, Card, Button } from "@rneui/themed";
import BootstrapStyleSheet from "react-native-bootstrap-styles";
import { useNavigation } from "@react-navigation/native";
const bootstrapStyleSheet = new BootstrapStyleSheet();
const { s, c } = bootstrapStyleSheet;
const MomoRegister = ({ route, navigation }) => {
  const { mtn_id } = route.params;
        const momo_URL =
          "https://info307-production.up.railway.app/account/register/";

        const [phoneNumber, setPhoneNumber] = useState("");
        const [password, setPassword] = useState("");
        const [momoAccount, SetMomoAccount] = useState(mtn_id);

    const create_momo = (event) => {
      event.preventDefault();
      axios
        .post(momo_URL, {
          password: password,
          phone_number: phoneNumber,
          mtn_account: momoAccount,
        })
        .then((response) => {
          console.log(response.data);
          navigation.navigate("Login");
        })
        .catch((error) => {
          console.log(error);
        });
    };
  return (
    <SafeAreaView>
      <View style={[s.container]}>
        <Card>
          <Card.Title>Momo Registration</Card.Title>
          <Card.Divider />
         <TextInput
          style={styles.input}
          value={phoneNumber}
          onChangeText={(e) => setPhoneNumber(e)}
          placeholder="Phone Number"
          keyboardType="numeric"
        />
        <TextInput
          style={styles.input}
          value={password}
          onChangeText={(e) => setPassword(e)}
          placeholder="Password"
          keyboardType="numeric"
        />
        <Button title="Register" onPress={create_momo} />
        <Button
          title="Register as Agent"
          onPress={() =>
            navigation.navigate("AgentRegister", { mtn_id: mtn_id })
          }
        /> 
        </Card>
      </View>
    </SafeAreaView>
  );
};
const styles = StyleSheet.create({
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
});
export default MomoRegister