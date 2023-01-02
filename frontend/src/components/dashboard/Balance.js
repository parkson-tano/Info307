import { View, StyleSheet } from 'react-native'
import React from 'react'
import { Card, ListItem, Button, Icon, Text } from "@rneui/themed";
import BootstrapStyleSheet from 'react-native-bootstrap-styles';
import { useNavigation } from "@react-navigation/native";
import { AuthContext } from '../context/AuthContext';
import { AuthProvider } from '../context/AuthContext';
const bootstrapStyleSheet = new BootstrapStyleSheet();
const { s, c } = bootstrapStyleSheet;

const Balance = () => {
  const navigation = useNavigation();
  const fxn = () => {
   navigation.navigate("Transaction");
  }
  console.log("Auth:", AuthContext)
    console.log("Provider:", AuthContext._currentValue.authState.access);
        console.log("Provider:", AuthContext._currentValue.authState.refresh);
  return (
    <View>
      <Card containerStyle={{borderRadius:15, padding:20}}>
        <Card.Title>XAF 450,00</Card.Title>
        <Card.Divider />
        <View>
          <View style={styles.container}>
            <View style={styles.item1}>
              <Text
                style={{
                  fontSize: 18,
                  fontWeight: "bold",
                  marginBottom: 0,
                }}
              >
                Last Transaction
              </Text>
            </View>
            <View style={styles.item2}>
              <Button
                buttonStyle={{
                  borderRadius: 0,
                  marginLeft: 0,
                  marginRight: 0,
                  marginBottom: 5,
                }}
                type="clear"
                onPress={fxn}
              >
                <Text
                  style={{ color: "orange", fontSize: 20, fontWeight: "bold" }}
                >
                  See More
                </Text>

                <Icon name="chevron-right" color="orange" />
              </Button>
            </View>
          </View>

          <View style={styles.container}>
            <View style={{ width: "20%" }}>
              <Icon type="evilicon" name="user" color="purple" raised reverse />
            </View>
            <View style={{ width: "40%" }}>
              <Text
                style={{ fontWeight: "bold", marginBottom: 10, fontSize: 17 }}
              >
                {"Deposit"}
              </Text>
              <Text
                style={{ marginBottom: 10, textAlign: "left", fontSize: 17 }}
              >
                {"674128573"}
              </Text>
            </View>
            <View style={{ width: "40%" }}>
              <Text
                style={{
                  fontWeight: "bold",
                  marginBottom: 10,
                  textAlign: "right",
                  fontSize: 17,
                }}
              >
                {"-2444"}XAF
              </Text>
              <Text
                style={{ marginBottom: 10, textAlign: "right", fontSize: 17 }}
              >
                {"4:34PM"}
              </Text>
            </View>
          </View>
        </View>
      </Card>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    flexWrap: "wrap",
    alignItems: "flex-start", // if you want to fill rows left to right
  },
  item1: {
    width: "60%",
    marginVertical: 10,
    // is 50% of container width
  },
  item2: {
    width: "40%",
    marginVertical: 10,
    // is 50% of container width
  },
});

export default Balance