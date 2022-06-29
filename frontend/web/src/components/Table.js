import React from "react";

function Table(props){
    return(
        <table class="table">
              <thead>
                {props.headings.map(heading => (
                    <th scope="col">{heading.charAt(0).toUpperCase() + heading.slice(1)}</th>
                ))}
              </thead>
              <tbody>
              {props.dataset.map( k => (
                  <tr>
                    {Object.values(k).map( item => (
                        <td>{item}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
        </table>
    )
}

export default Table;