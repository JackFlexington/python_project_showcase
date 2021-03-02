// Program: index.js
// Author: Jacob Storer
// Last Reviewed: 03/01/2021

// Libraries
import React from 'react';
import { render } from 'react-dom';
import 'carbon-components/css/carbon-components.min.css';
import { DataTable, TableContainer, Table, TableHead, TableRow, TableHeader, TableBody, TableCell } from 'carbon-components-react';
import { headerData, rowData } from './sampleData';

// Initialize app
const App = () => (
<DataTable rows={rowData} headers={headerData} isSortable>
{({ rows, headers, getHeaderProps, getTableProps }) => (
  <TableContainer title="Weekly Payroll Report">
    <Table {...getTableProps()} useZebraStyles size='normal'>
      <TableHead>
        <TableRow>
          {headers.map((header) => (
            <TableHeader {...getHeaderProps({ header })}>
              {header.header}
            </TableHeader>
          ))}
        </TableRow>
      </TableHead>
      <TableBody>
        {rows.map((row) => (
          <TableRow key={row.id}>
            {row.cells.map((cell) => (
              <TableCell key={cell.id}>{cell.value}</TableCell>
            ))}
          </TableRow>
        ))}
      </TableBody>
    </Table>
  </TableContainer>
)}
</DataTable>
);

// Run app
render(<App />, document.getElementById('root'));