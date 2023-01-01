import { View, Text } from "react-native";
import React from "react";
import Icon from "react-native-vector-icons/FontAwesome";
import { Input, Card, Button } from "@rneui/themed";
import BootstrapStyleSheet from "react-native-bootstrap-styles";
import { useNavigation } from "@react-navigation/native";
const bootstrapStyleSheet = new BootstrapStyleSheet();
const { s, c } = bootstrapStyleSheet;
const FundTransfer = () => {
  return (
    <View style={[s.container]}>
      <Card>
        <Card.Title>Transfer Money</Card.Title>
        <Card.Divider />
        <Input
          placeholder="Enter Momo Number"
          rightIcon={{ type: "font-awesome", name: "chevron-right" }}
          keyboardType="numeric"
        />
        <Input
          placeholder="Enter Amount"
          rightIcon={{ type: "font-awesome", name: "chevron-right" }}
          keyboardType="numeric"
        />
        <Button title={"Proceed"} />
      </Card>
    </View>
  );
};

export default FundTransfer;
