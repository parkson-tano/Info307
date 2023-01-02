import { View, Text, ActivityIndicator, ScrollView } from "react-native";
import React, { useState, useEffect, useContext } from "react";
import Icon from "react-native-vector-icons/FontAwesome";
import { Input, Card, Button } from "@rneui/themed";
import BootstrapStyleSheet from "react-native-bootstrap-styles";
import { useNavigation } from "@react-navigation/native";
import { AuthProvider } from "./context/AuthContext";
import axios from "axios";
import { AuthContext } from "./context/AuthContext";
import jwt_decode from "jwt-decode";


const bootstrapStyleSheet = new BootstrapStyleSheet();

const { s, c } = bootstrapStyleSheet;
const TopOther = ({navigation}) => {
  const user = jwt_decode(AuthContext._currentValue.authState.access);
  const [balance, setBalance] = useState("");
  const [newBalance, setNewBalance] = useState("");
  const [amount, setAmount] = useState("");
  const [btn, setBtn] = useState(false);
  const [phoneNumber, setPhoneNumber] = useState('')
  const balance_info = `https://info307-production.up.railway.app/accountbalance/${user.user_id}`;
  const airtime_url = "https://info307-production.up.railway.app/airtime";
  const [submitting, setSubmitting] = useState(false);
  const isSubmitting = () => {
    setSubmitting(true);
    setBtn(true);
  };
  useEffect(() => {
    axios
      .get(balance_info)
      .then((response) => {
        setBalance(response.data);
      })
      .catch((error) => console.log(error));
  }, []);
  const new_ba = parseInt(balance.balance) - parseInt(amount);
  const buy_credit = async () => {
    isSubmitting();
    axios.post(airtime_url, {
      number: phoneNumber,
      amount: amount,
      user: user.user_id,
    });
    axios.patch(balance_info, {
      balance: new_ba,
    });
    navigation.navigate("Home");
  };

  return (
    <View style={[s.container]}>
      <Card>
        <Card.Title>Buy Credit for You</Card.Title>
        <Card.Divider />
        <Card.Title style={{ fontSize: 18 }}>{balance.balance}</Card.Title>
        <Input
          placeholder="Enter Phone Number"
          rightIcon={{ type: "font-awesome", name: "chevron-right" }}
          keyboardType="numeric"
          value={phoneNumber}
          onChangeText={(e) => setPhoneNumber(e)}
        />
        <Input
          placeholder="Enter Amount"
          rightIcon={{ type: "font-awesome", name: "chevron-right" }}
          keyboardType="numeric"
          value={amount}
          onChangeText={(e) => setAmount(e)}
        />
        {amount > balance.balance ? (
          <Text style={{ color: "red" }}>Insufficient amount</Text>
        ) : (
          ""
        )}
        {submitting && (
          <ActivityIndicator
            size="large"
            color="#0066CC"
            style={{ padding: 10 }}
          />
        )}
        <Button
          title={"Buy Credit"}
          onPress={buy_credit}
          disabled={amount > balance.balance ? true : false || btn}
        />
      </Card>
    </View>
  );
};

export default TopOther;
