'use client'
import { useEffect, useState } from 'react';

// Define the TypeScript type for the data you'll be fetching
interface DataItem {
  id: number;
  name: string;
  // Add other fields here...
}

const Home = () => {
  const [data, setData] = useState<DataItem[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/data')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        setError('Error fetching data');
        setLoading(false);
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Data from Python Backend</h1>
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>{error}</p>
      ) : data.length === 0 ? (
        <p>No data available</p>
      ) : (
        <ul>
          {data.map((item) => (
            <li key={item.id}>
              {item.name} {/* Adjust based on your data structure */}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Home;
