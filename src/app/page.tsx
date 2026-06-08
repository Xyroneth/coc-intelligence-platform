"use client";

import { useState } from "react";
import api from "../lib/api";

export default function Home() {
  const [playerTag, setPlayerTag] = useState("");
  const [player, setPlayer] = useState<any>(null);

  const [clanTag, setClanTag] = useState("");
  const [clan, setClan] = useState<any>(null);

  const searchPlayer = async () => {
    try {
      const res = await api.get(`/player/${playerTag}`);
      setPlayer(res.data);
    } catch (error) {
      console.error(error);
      alert("Player not found");
    }
  };

  const searchClan = async () => {
    try {
      const res = await api.get(`/clan/${clanTag}`);
      console.log("CLAN DATA:", res.data);
      setClan(res.data);
    } catch (error) {
      console.error(error);
      alert("Clan not found");
    }
  };

  return (
    <div
      style={{
        backgroundColor: "#0f172a",
        minHeight: "100vh",
        color: "white",
        padding: "30px",
        fontFamily: "Arial",
      }}
    >
      <h1>🛡️ CoC Intelligence Platform</h1>

      <hr />

      <h2>Player Search</h2>

      <input
        value={playerTag}
        onChange={(e) => setPlayerTag(e.target.value)}
        placeholder="Enter Player Tag"
        style={{
          padding: "10px",
          width: "250px",
          color: "black",
        }}
      />

      <button
        onClick={searchPlayer}
        style={{
          marginLeft: "10px",
          padding: "10px",
          cursor: "pointer",
        }}
      >
        Search Player
      </button>

      {player && (
        <div
          style={{
            marginTop: "20px",
            padding: "20px",
            border: "1px solid gray",
            borderRadius: "10px",
            backgroundColor: "#1e293b",
          }}
        >
          <h2>{player.name}</h2>

          <p>
            <strong>Tag:</strong> {player.tag}
          </p>

          <p>
            <strong>Town Hall:</strong> {player.townHallLevel}
          </p>

          <p>
            <strong>Trophies:</strong> {player.trophies}
          </p>

          <p>
            <strong>XP Level:</strong> {player.expLevel}
          </p>
        </div>
      )}

      <hr style={{ marginTop: "40px" }} />

      <h2>Clan Search</h2>

      <input
        value={clanTag}
        onChange={(e) => setClanTag(e.target.value)}
        placeholder="Enter Clan Tag"
        style={{
          padding: "10px",
          width: "250px",
          color: "black",
        }}
      />

      <button
        onClick={searchClan}
        style={{
          marginLeft: "10px",
          padding: "10px",
          cursor: "pointer",
        }}
      >
        Search Clan
      </button>

      {clan && (
        <div
          style={{
            marginTop: "25px",
            padding: "25px",
            border: "1px solid #334155",
            borderRadius: "15px",
            backgroundColor: "#1e293b",
          }}
        >
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: "20px",
              marginBottom: "20px",
            }}
          >
            <img
              src={clan.badgeUrls?.medium}
              alt="Clan Badge"
              width={100}
              height={100}
            />

            <div>
              <h1>{clan.name}</h1>

              <p>
                <strong>Tag:</strong> {clan.tag}
              </p>

              <p>
                <strong>Description:</strong> {clan.description}
              </p>
            </div>
          </div>

          <hr />

          <h2>Clan Statistics</h2>

          <p>
            <strong>Clan Level:</strong> {clan.clanLevel}
          </p>

          <p>
            <strong>Members:</strong> {clan.members}
          </p>

          <p>
            <strong>War Wins:</strong> {clan.warWins}
          </p>

          <p>
            <strong>War Win Streak:</strong> {clan.warWinStreak}
          </p>

          <p>
            <strong>Required Trophies:</strong>{" "}
            {clan.requiredTrophies}
          </p>

          <p>
            <strong>Location:</strong>{" "}
            {clan.location?.name}
          </p>

          <hr />

          <h2>Top Clan Members</h2>

          <table
            style={{
              width: "100%",
              borderCollapse: "collapse",
            }}
          >
            <thead>
              <tr>
                <th align="left">Name</th>
                <th align="left">Role</th>
                <th align="left">TH</th>
                <th align="left">XP</th>
              </tr>
            </thead>

            <tbody>
              {clan.memberList?.slice(0, 10).map(
                (member: any) => (
                  <tr key={member.tag}>
                    <td>{member.name}</td>
                    <td>{member.role}</td>
                    <td>{member.townHallLevel}</td>
                    <td>{member.expLevel}</td>
                  </tr>
                )
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}